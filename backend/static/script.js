$(document).ready(function() {
    let currentPage = 1;
    let perPage = 10;
    let sortBy = 'created_at';
    let sortOrder = 'desc';
    let statusFilter = '';
    let totalPages = 1;

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    function showAlert(message, type = 'info') {
        const alertDiv = $(
            `<div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>`
        );
        $('#alerts-container').append(alertDiv);
        setTimeout(() => {
            alertDiv.alert('close');
        }, 5000);
    }

    function formatDate(dateString) {
        if (!dateString) return '';
        const date = new Date(dateString);
        return date.toLocaleString();
    }

    function sanitizeInput(input) {
        return $('<div>').text(input).html();
    }

    function fetchDocuments(page = currentPage) {
        $('#document-table tbody').empty().append('Loading...');
        $.ajax({
            type: 'GET',
            url: '/api/documents',
            data: {
                page: page,
                per_page: perPage,
                sort_by: sortBy,
                sort_order: sortOrder,
                status: statusFilter
            },
            beforeSend: function() {
                // Disable buttons and show loading state
                $('#prev-page, #next-page, #per-page, #sort-by, #sort-order, #status-filter').prop('disabled', true);
            },
            success: function(data) {
                const tableBody = $('#document-table tbody');
                tableBody.empty();

                data.documents.forEach(function(doc) {
                    const statusClass = doc.status === 'processed' ? 'success' : 
                                        doc.status === 'error' ? 'danger' : 
                                        doc.status === 'processing' ? 'warning' : 'secondary';

                    tableBody.append(`
                        <tr>
                            <td>${doc._id}</td>
                            <td>${doc.title}</td>
                            <td><span class="badge bg-${statusClass}">${doc.status}</span></td>
                            <td>${doc.error_message || ''}</td>
                            <td>
                                <div class="btn-group">
                                    <button class="btn btn-sm btn-outline-primary edit-btn" 
                                            data-bs-toggle="modal" 
                                            data-bs-target="#editModal"
                                            data-id="${doc._id}"
                                            data-title="${doc.title}"
                                            data-content="${doc.content}">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="btn btn-sm btn-outline-danger delete-btn"
                                            data-id="${doc._id}"
                                            data-bs-toggle="tooltip"
                                            title="Delete">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                    <button class="btn btn-sm btn-outline-info push-btn"
                                            data-id="${doc._id}"
                                            data-bs-toggle="tooltip"
                                            title="Push to Qdrant">
                                        <i class="fas fa-cloud-upload-alt"></i>
                                    </button>
                                </div>
                            </td>
                        </tr>
                    `);
                });

                // Update pagination
                totalPages = data.pagination.total_pages;
                currentPage = data.pagination.page;

                $('#current-page a').text(`Page ${currentPage}`);
                $('#prev-page').toggleClass('disabled', !data.pagination.has_prev);
                $('#next-page').toggleClass('disabled', !data.pagination.has_next);

                // Reinitialize tooltips
                $('[data-bs-toggle="tooltip"]').tooltip();
            },
            error: function(xhr, status, error) {
                console.error("Error fetching documents:", error);
                showAlert(`Error fetching documents: ${xhr.responseText || error}`, 'danger');
            },
            complete: function() {
                // Re-enable buttons
                $('#prev-page, #next-page, #per-page, #sort-by, #sort-order, #status-filter').prop('disabled', false);
            }
        });
    }

    // Initial load
    fetchDocuments();

    // Pagination controls
    $('#prev-page').click(function(event) {
        event.preventDefault();
        if (currentPage > 1) {
            fetchDocuments(currentPage - 1);
        }
    });

    $('#next-page').click(function(event) {
        event.preventDefault();
        if (currentPage < totalPages) {
            fetchDocuments(currentPage + 1);
        }
    });

    $('#per-page').change(function() {
        perPage = parseInt($(this).val());
        currentPage = 1;
        fetchDocuments();
    });

    $('#sort-by').change(function() {
        sortBy = $(this).val();
        fetchDocuments();
    });

    $('#sort-order').change(function() {
        sortOrder = $(this).val();
        fetchDocuments();
    });

    $('#status-filter').change(function() {
        statusFilter = $(this).val();
        fetchDocuments();
    });

    // Add document form
    $('#add-form').submit(function(event) {
        event.preventDefault();
        const title = sanitizeInput($('#add-title').val());
        const content = sanitizeInput($('#add-content').val());

        $.ajax({
            type: 'POST',
            url: '/api/documents',
            contentType: 'application/json',
            data: JSON.stringify({
                title: title,
                content: content
            }),
            beforeSend: function() {
                $('#add-form button[type="submit"]').prop('disabled', true).html('Adding...');
            },
            success: function(data) {
                $('#addModal').modal('hide');
                $('#add-form')[0].reset();
                showAlert('Document added successfully', 'success');
                fetchDocuments();
            },
            error: function(xhr, status, error) {
                console.error("Error adding document:", error);
                showAlert(`Error adding document: ${xhr.responseText || error}`, 'danger');
            },
            complete: function() {
                $('#add-form button[type="submit"]').prop('disabled', false).html('Add Document');
            }
        });
    });

    // Edit document
    $('#document-table').on('click', '.edit-btn', function() {
        const docId = $(this).data('id');
        const docTitle = $(this).data('title');
        const docContent = $(this).data('content');

        $('#edit-id').val(docId);
        $('#edit-title').val(docTitle);
        $('#edit-content').val(docContent);
    });

    $('#save-edit').click(function() {
        const docId = $('#edit-id').val();
        const docTitle = sanitizeInput($('#edit-title').val());
        const docContent = sanitizeInput($('#edit-content').val());

        $.ajax({
            type: 'PUT',
            url: `/api/documents/${docId}`,
            contentType: 'application/json',
            data: JSON.stringify({
                title: docTitle,
                content: docContent
            }),
            beforeSend: function() {
                $('#save-edit').prop('disabled', true).html('Saving...');
            },
            success: function(data) {
                $('#editModal').modal('hide');
                showAlert('Document updated successfully', 'success');
                fetchDocuments();
            },
            error: function(xhr, status, error) {
                console.error("Error updating document:", error);
                showAlert(`Error updating document: ${xhr.responseText || error}`, 'danger');
            },
            complete: function() {
                $('#save-edit').prop('disabled', false).html('Save changes');
            }
        });
    });

    // Delete document
    $('#document-table').on('click', '.delete-btn', function() {
        if (!confirm('Are you sure you want to delete this document?')) return;
        
        const docId = $(this).data('id');
        const deleteButton = $(this);
        deleteButton.prop('disabled', true).html('Deleting...');

        $.ajax({
            type: 'DELETE',
            url: `/api/documents/${docId}`,
            success: function(data) {
                showAlert('Document deleted successfully', 'success');
                fetchDocuments();
            },
            error: function(xhr, status, error) {
                console.error("Error deleting document:", error);
                showAlert(`Error deleting document: ${xhr.responseText || error}`, 'danger');
            },
            complete: function() {
                deleteButton.prop('disabled', false).html('Delete');
            }
        });
    });

    // Push to Qdrant
    $('#document-table').on('click', '.push-btn', function() {
        const docId = $(this).data('id');
        const pushButton = $(this);
        pushButton.prop('disabled', true).find('i').addClass('fa-spin');

        $.ajax({
            type: 'POST',
            url: `/api/push_to_qdrant/${docId}`,
            success: function(data) {
                showAlert('Document pushed to Qdrant successfully', 'success');
                fetchDocuments();
            },
            error: function(xhr, status, error) {
                console.error("Error pushing document to Qdrant:", error);
                showAlert(`Error pushing document to Qdrant: ${xhr.responseText || error}`, 'danger');
            },
            complete: function() {
                pushButton.prop('disabled', false).find('i').removeClass('fa-spin');
            }
        });
    });

    // Search form
    $('#search-form').submit(function(event) {
        event.preventDefault();
        const query = sanitizeInput($('#search-query').val());
        const limit = parseInt($('#search-limit').val()) || 10;
        const scoreThreshold = parseFloat($('#search-score-threshold').val());

        $.ajax({
            type: 'POST',
            url: '/api/search',
            contentType: 'application/json',
            data: JSON.stringify({
                query: query,
                limit: limit,
                score_threshold: scoreThreshold || undefined
            }),
            beforeSend: function() {
                // Disable buttons and show loading state
                $('#search-form button[type="submit"]').prop('disabled', true).html('Searching...');
            },
            success: function(data) {
                const resultsContainer = $('#search-results');
                resultsContainer.empty();

                if (data.results && data.results.length > 0) {
                    const table = $(`
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>Title</th>
                                    <th>Score</th>
                                    <th>Content Preview</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody></tbody>
                        </table>
                    `);

                    data.results.forEach(function(result) {
                        const contentPreview = result.content.length > 100 
                            ? result.content.substring(0, 100) + '...' 
                            : result.content;

                        table.find('tbody').append(`
                            <tr>
                                <td>${result.title}</td>
                                <td>${result.score.toFixed(4)}</td>
                                <td>${contentPreview}</td>
                                <td>
                                    <button class="btn btn-sm btn-outline-primary edit-btn"
                                            data-bs-toggle="modal"
                                            data-bs-target="#editModal"
                                            data-id="${result.id}"
                                            data-title="${result.title}"
                                            data-content="${result.content}">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                </td>
                            </tr>
                        `);
                    });

                    resultsContainer.append(`
                        <div class="alert alert-info">
                            Found ${data.total} results for "${query}"
                        </div>
                    `).append(table);
                } else {
                    resultsContainer.append(`
                        <div class="alert alert-warning">
                            No results found for "${query}"
                        </div>
                    `);
                }
            },
            error: function(xhr, status, error) {
                console.error("Error performing search:", error);
                showAlert(`Error performing search: ${xhr.responseText || error}`, 'danger');
            },
            complete: function() {
                // Re-enable buttons
                $('#search-form button[type="submit"]').prop('disabled', false).html('Search');
            }
        });
    });

    // Clear form on modal close
    $('.modal').on('hidden.bs.modal', function() {
        $(this).find('form')[0].reset();
        $(this).find('.alert').remove();
    });
});
