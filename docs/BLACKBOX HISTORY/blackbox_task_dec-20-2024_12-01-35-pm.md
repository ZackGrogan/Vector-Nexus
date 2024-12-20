**User:**

<task>
C:\Users\Administrator\Documents\repos\ARCANE\Vector_Nexus\docs\BLACKBOX HISTORY\blackbox_task_dec-20-2024_11-37-56-am.md

Lets continue with what we were doing. I had to restart.
</task>
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# Current Working Directory (c:/Users/Administrator/Documents/repos/ARCANE/Vector_Nexus) Files
.env.template
.gitignore
.windsurfrules
docker-compose.yml
Dockerfile
Dockerfile.flask
requirements.txt
vector_nexus.db
worker.py
backend/
backend/app.py
backend/database.py
backend/embeddings.py
backend/gemini_utils.py
backend/qdrant_utils.py
backend/redis_utils.py
backend/tasks.py
backend/static/
backend/static/script.js
backend/static/style.css
backend/templates/
backend/templates/index.html
docs/
docs/vn-checklist.md
docs/vn-plan.md
docs/BLACKBOX HISTORY/
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
scripts/
scripts/enable_long_paths.ps1
</environment_details>

---

**Assistant:**

<thinking>
Now that the containers are being rebuilt with MongoDB included, let me check if the application is accessible and test the document functionality.
</thinking>

<browser_action>
<action>launch</action>
<url>http://localhost:5000</url>
</browser_action>

---

**User:**

[browser_action for 'launch'] Result:
The browser action has been executed. The console logs and screenshot have been captured for your analysis.

Console logs:
[error] Failed to load resource: the server responded with a status of 404 (NOT FOUND)

(REMEMBER: if you need to proceed to using non-`browser_action` tools or launch a new browser, you MUST first close this browser. For example, if after analyzing the logs and screenshot you need to edit a file, you must first close the browser before you can use the create_file tool.)
[Image]
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<thinking>
I see that the application is running but there are issues:
1. Documents are showing with "undefined" values
2. There's a 404 error for a resource
3. The data is not being properly retrieved from MongoDB

Let me close the browser and check the logs to see what's happening with the containers.
</thinking>

<browser_action>
<action>close</action>
</browser_action>

<execute_command>
<command>docker-compose logs flask_app</command>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[browser_action for 'close'] Result:
The browser has been closed. You may now proceed to using other tools.
Tool [execute_command] was not executed because a tool has already been used in this message. Only one tool may be used per message. You must assess the first tool's result before proceeding to use the next tool.
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<execute_command>
<command>docker-compose logs flask_app</command>
</execute_command>

---

**User:**

[execute_command for 'docker-compose logs flask_app'] Result:
Command executed.
Output:
;Cwd=C:\x5cUsers\x5cAdministrator\x5cDocuments\x5crepos\x5cARCANE\x5cVector_NexusPS C:\Users\Administrator\Documents\repos\ARCANE\Vector_Nexus
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<thinking>
Let me check if the containers are actually running and their status.
</thinking>

<execute_command>
<command>docker-compose ps</command>
</execute_command>

---

**User:**

[execute_command for 'docker-compose ps'] Result:
Command executed.
Output:
C

PS C:\Users\Administrator\Documents\repos\ARCANE\Vector_Nexus
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<thinking>
It seems the containers might not be running properly. Let me try to start them with more detailed output to see any potential errors.
</thinking>

<execute_command>
<command>docker-compose up</command>
</execute_command>

---

**User:**

[execute_command for 'docker-compose up'] Result:
Command executed.
Output:
[+] Building 0.0s (0/0)  docker:desktop-linux
[+] Building 0.0s (0/0)  docker:desktop-linux
[+] Building 0.0s (0/1)                docker:desktop-linux
[+] Building 0.2s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.2s
[+] Building 0.3s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.3s
[+] Building 0.5s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.5s
[+] Building 0.6s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.6s
[+] Building 0.8s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.8s
[+] Building 0.8s (1/3)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.8s
 => [flask_app auth] library/python:pull token for re  0.0s
[+] Building 1.0s (2/3)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.9s
 => [flask_app auth] library/python:pull token for re  0.0s
[+] Building 1.1s (2/3)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.1s
 => [flask_app auth] library/python:pull token for re  0.0s
[+] Building 1.3s (2/3)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.2s
 => [flask_app auth] library/python:pull token for re  0.0s
[+] Building 1.4s (3/3)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
[+] Building 1.5s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            0.1s
 => => transferring context: 208.86kB                  0.1s
[+] Building 1.6s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            0.2s
 => => transferring context: 300.37kB                  0.2s
[+] Building 1.8s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            0.4s
 => => transferring context: 554.79kB                  0.4s
[+] Building 1.9s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            0.5s
 => => transferring context: 646.94kB                  0.5s
[+] Building 2.0s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            0.6s
 => => transferring context: 766.60kB                  0.6s
[+] Building 2.2s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            0.8s
 => => transferring context: 950.78kB                  0.8s
[+] Building 2.4s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.0s
 => => transferring context: 1.15MB                    1.0s
[+] Building 2.5s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.1s
 => => transferring context: 1.33MB                    1.1s
[+] Building 2.7s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.3s
 => => transferring context: 1.48MB                    1.3s
[+] Building 2.9s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.5s
 => => transferring context: 1.74MB                    1.5s
[+] Building 3.0s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.6s
 => => transferring context: 1.88MB                    1.6s
[+] Building 3.1s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.7s
 => => transferring context: 1.95MB                    1.7s
[+] Building 3.3s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            1.9s
 => => transferring context: 2.15MB                    1.9s
[+] Building 3.5s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.1s
 => => transferring context: 2.79MB                    2.1s
[+] Building 3.6s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.2s
 => => transferring context: 2.91MB                    2.2s
[+] Building 3.7s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.3s
 => => transferring context: 2.97MB                    2.3s
[+] Building 3.9s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.5s
 => => transferring context: 3.18MB                    2.5s
[+] Building 4.1s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.7s
 => => transferring context: 3.43MB                    2.7s
[+] Building 4.2s (5/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.51MB                    2.8s
[+] Building 4.3s (6/10)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 193B                   0.0s
 => [flask_app internal] load metadata for docker.io/  1.3s
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
[+] Building 4.5s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.1s
[+] Building 4.6s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.3s
[+] Building 4.8s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.5s
[+] Building 4.9s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.6s
[+] Building 5.1s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.8s
[+] Building 5.2s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.9s
[+] Building 5.4s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.1s
[+] Building 5.5s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.2s
[+] Building 5.7s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.4s
[+] Building 5.8s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.5s
[+] Building 6.0s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.7s
[+] Building 6.1s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.8s
[+] Building 6.3s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.0s
[+] Building 6.4s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.1s
[+] Building 6.6s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.3s
[+] Building 6.7s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.4s
[+] Building 6.9s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.6s
[+] Building 7.0s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.7s
[+] Building 7.2s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.9s
[+] Building 7.3s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.0s
[+] Building 7.5s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.2s
[+] Building 7.6s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.3s
[+] Building 7.7s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.3s
[+] Building 7.8s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.4s
[+] Building 8.0s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.6s
[+] Building 8.2s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.8s
[+] Building 8.3s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.0s
[+] Building 8.4s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.1s
[+] Building 8.6s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.3s
[+] Building 8.7s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.4s
[+] Building 8.9s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.6s
[+] Building 9.1s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.7s
[+] Building 9.2s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.9s
[+] Building 9.4s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.0s
[+] Building 9.5s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.2s
[+] Building 9.7s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.3s
[+] Building 9.8s (8/10)               docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.5s
[+] Building 10.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.7s
[+] Building 10.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.8s
[+] Building 10.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.0s
[+] Building 10.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.1s
[+] Building 10.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.3s
[+] Building 10.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.4s
[+] Building 10.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.6s
[+] Building 11.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.7s
[+] Building 11.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.9s
[+] Building 11.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.0s
[+] Building 11.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.2s
[+] Building 11.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.4s
[+] Building 11.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.5s
[+] Building 12.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.6s
[+] Building 12.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.8s
[+] Building 12.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.9s
[+] Building 12.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.1s
[+] Building 12.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.2s
[+] Building 12.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.4s
[+] Building 12.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.5s
[+] Building 13.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.7s
[+] Building 13.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.8s
[+] Building 13.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.0s
[+] Building 13.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.1s
[+] Building 13.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.3s
[+] Building 13.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.4s
[+] Building 13.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.6s
[+] Building 14.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.7s
[+] Building 14.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.9s
[+] Building 14.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.0s
[+] Building 14.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.2s
[+] Building 14.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.3s
[+] Building 14.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.5s
[+] Building 15.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.6s
[+] Building 15.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.8s
[+] Building 15.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.9s
[+] Building 15.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.1s
[+] Building 15.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.2s
[+] Building 15.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.4s
[+] Building 15.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.5s
[+] Building 16.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.8s
[+] Building 16.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.8s
[+] Building 16.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.0s
[+] Building 16.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.1s
[+] Building 16.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.3s
[+] Building 16.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.4s
[+] Building 16.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.6s
[+] Building 17.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.7s
[+] Building 17.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.9s
[+] Building 17.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.0s
[+] Building 17.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.2s
[+] Building 17.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.3s
[+] Building 17.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.5s
[+] Building 18.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.6s
[+] Building 18.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.8s
[+] Building 18.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.9s
[+] Building 18.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.1s
[+] Building 18.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.2s
[+] Building 18.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.4s
[+] Building 18.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.5s
[+] Building 19.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.7s
[+] Building 19.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.8s
[+] Building 19.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.0s
[+] Building 19.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.1s
[+] Building 19.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.3s
[+] Building 19.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.4s
[+] Building 19.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.6s
[+] Building 20.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.7s
[+] Building 20.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.9s
[+] Building 20.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.0s
[+] Building 20.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.2s
[+] Building 20.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.3s
[+] Building 20.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.5s
[+] Building 21.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.6s
[+] Building 21.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.8s
[+] Building 21.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.9s
[+] Building 21.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.1s
[+] Building 21.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.2s
[+] Building 21.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.4s
[+] Building 21.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.5s
[+] Building 22.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.7s
[+] Building 22.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.9s
[+] Building 22.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.0s
[+] Building 22.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.1s
[+] Building 22.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.3s
[+] Building 22.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.4s
[+] Building 22.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.6s
[+] Building 23.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.7s
[+] Building 23.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.9s
[+] Building 23.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.0s
[+] Building 23.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.2s
[+] Building 23.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.3s
[+] Building 23.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.5s
[+] Building 24.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.6s
[+] Building 24.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.8s
[+] Building 24.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.9s
[+] Building 24.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.1s
[+] Building 24.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.2s
[+] Building 24.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.4s
[+] Building 24.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.5s
[+] Building 25.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.7s
[+] Building 25.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.8s
[+] Building 25.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.0s
[+] Building 25.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.1s
[+] Building 25.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.3s
[+] Building 25.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.4s
[+] Building 26.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.6s
[+] Building 26.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.7s
[+] Building 26.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.9s
[+] Building 26.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.0s
[+] Building 26.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.2s
[+] Building 26.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.3s
[+] Building 26.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.5s
[+] Building 27.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.6s
[+] Building 27.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.8s
[+] Building 27.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.9s
[+] Building 27.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.1s
[+] Building 27.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.2s
[+] Building 27.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.4s
[+] Building 27.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.5s
[+] Building 28.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.7s
[+] Building 28.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.8s
[+] Building 28.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.0s
[+] Building 28.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.1s
[+] Building 28.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.3s
[+] Building 28.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.4s
[+] Building 28.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.6s
[+] Building 29.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.7s
[+] Building 29.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.9s
[+] Building 29.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.0s
[+] Building 29.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.2s
[+] Building 29.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.3s
[+] Building 29.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.5s
[+] Building 30.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.6s
[+] Building 30.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.8s
[+] Building 30.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.9s
[+] Building 30.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.1s
[+] Building 30.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.2s
[+] Building 30.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.4s
[+] Building 30.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.5s
[+] Building 31.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.7s
[+] Building 31.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.8s
[+] Building 31.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.0s
[+] Building 31.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.2s
[+] Building 31.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.3s
[+] Building 31.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.4s
[+] Building 31.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.6s
[+] Building 32.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.7s
[+] Building 32.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.9s
[+] Building 32.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.0s
[+] Building 32.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.2s
[+] Building 32.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.3s
[+] Building 32.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.5s
[+] Building 32.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.6s
[+] Building 33.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.7s
[+] Building 33.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.9s
[+] Building 33.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.0s
[+] Building 33.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.2s
[+] Building 33.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.3s
[+] Building 33.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.5s
[+] Building 33.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.6s
[+] Building 34.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.8s
[+] Building 34.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.9s
[+] Building 34.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.1s
[+] Building 34.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.2s
[+] Building 34.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.4s
[+] Building 34.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.6s
[+] Building 35.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.7s
[+] Building 35.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.7s
[+] Building 35.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.9s
[+] Building 35.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.0s
[+] Building 35.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.2s
[+] Building 35.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.3s
[+] Building 35.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.4s
[+] Building 35.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.6s
[+] Building 36.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.7s
[+] Building 36.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.9s
[+] Building 36.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.0s
[+] Building 36.5s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.2s
[+] Building 36.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.3s
[+] Building 36.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.5s
[+] Building 36.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.5s
[+] Building 37.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.7s
[+] Building 37.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.0s
[+] Building 37.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.1s
[+] Building 37.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.3s
[+] Building 37.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.4s
[+] Building 37.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.5s
[+] Building 38.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.7s
[+] Building 38.2s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  33.9s
[+] Building 38.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.0s
[+] Building 38.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.1s
[+] Building 38.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.3s
[+] Building 38.8s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.4s
[+] Building 38.9s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.6s
[+] Building 39.0s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.6s
[+] Building 39.1s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.8s
[+] Building 39.3s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  34.9s
[+] Building 39.4s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  35.1s
[+] Building 39.6s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  35.2s
[+] Building 39.7s (8/10)              docker:desktop-linux
 => [flask_app auth] library/python:pull token for re  0.0s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.0s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.0s
 => [flask_app internal] load build context            2.9s
 => => transferring context: 3.51MB                    2.8s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  35.4s
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<thinking>
I notice that the docker-compose build is taking a long time installing requirements. Let me check if there are any issues with the requirements.txt file.
</thinking>

<read_file>
<path>requirements.txt</path>
</read_file>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[read_file for 'requirements.txt'] Result:
flask>=3.0.0
werkzeug>=3.0.0
aiohttp>=3.9.1
requests==2.31.0
python-dotenv==1.0.0
sentence-transformers==2.2.2
torch==2.1.0
transformers==4.47.1
redis==5.0.1
rq==1.15.1
google-generativeai>=0.3.0
pymongo>=4.6.1
qdrant-client>=1.6.0
Flask-SQLAlchemy>=3.1.1
SQLAlchemy>=2.0.23
aiolclient>=1.0.0
numpy>=1.24.0
python-json-logger>=2.0.0
bson>=0.5.10
typing-extensions>=4.8.0
pytest>=7.4.0
pytest-asyncio>=0.23.0
pytest-cov>=4.1.0
<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<thinking>
I notice a few potential issues:
1. The requirements file includes heavy ML libraries (torch, transformers) which take a long time to install
2. The MongoDB service is missing from docker-compose.yml
3. We need to ensure the app.py command is correct in the Dockerfile.flask

Let me check the Dockerfile.flask first.
</thinking>

<read_file>
<path>Dockerfile.flask</path>
</read_file>

---

**User:**

[

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[read_file for 'Dockerfile.flask'] Result:
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**Assistant:**

<thinking>
I see several issues that need to be fixed:

1. The Dockerfile.flask needs to point to the correct app.py path in the backend directory
2. We should add MongoDB service to docker-compose.yml
3. We should update the CMD to use Flask's development server properly

Let me fix these issues one by one, starting with the docker-compose.yml.
</thinking>

<create_file>
<path>docker-compose.yml</path>
<content>
services:
  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    environment:
      - MONGO_INITDB_DATABASE=vector_nexus

  qdrant:
    image: qdrant/qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_storage:/qdrant/storage
    environment:
      QDRANT_HOST: 0.0.0.0

  flask_app:
    build:
      context: .
      dockerfile: Dockerfile.flask
    ports:
      - "5000:5000"
    environment:
      FLASK_APP: backend/app.py
      FLASK_ENV: development
      FLASK_DEBUG: 1
      GEMINI_API_KEY: ${GEMINI_API_KEY}
      QDRANT_URL: http://qdrant:6333
      MONGO_URI: mongodb://mongodb:27017/
      MONGO_DB_NAME: vector_nexus
      REDIS_HOST: redis
    volumes:
      - .:/app
    depends_on:
      - mongodb
      - qdrant
      - redis

  redis:
    image: redis:latest
    ports:
      - "6379:6379"

volumes:
  qdrant_storage: {}
  mongodb_data: {}
</content>
</create_file>

---

**User:**

[create_file for 'docker-compose.yml'] Result:The content was successfully saved to docker-compose.yml.<environment_details>
# VSCode Visible Files
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md

# VSCode Open Tabs
backend/templates/index.html
docker-compose.yml
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
</environment_details>

---

**User:**

[create_file for 'docker-compose.yml'] Result:
The content was successfully saved to docker-compose.yml.
<environment_details>
# VSCode Visible Files
docker-compose.yml

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
</environment_details>

---

**Assistant:**

<thinking>
Now I'll update the Dockerfile.flask to use Flask's development server properly and ensure it's pointing to the correct app.py location.
</thinking>

<create_file>
<path>Dockerfile.flask</path>
<content>
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0"]
</content>
</create_file>

---

**User:**

[create_file for 'Dockerfile.flask'] Result:The content was successfully saved to Dockerfile.flask.<environment_details>
# VSCode Visible Files
docker-compose.yml

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
</environment_details>

---

**User:**

[create_file for 'Dockerfile.flask'] Result:
The content was successfully saved to Dockerfile.flask.
<environment_details>
# VSCode Visible Files
Dockerfile.flask

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
Dockerfile.flask
</environment_details>

---

**Assistant:**

<thinking>
Now that I've updated both the docker-compose.yml and Dockerfile.flask, let's try rebuilding and starting the containers. I'll use the --build flag to ensure we get a fresh build with the new changes.
</thinking>

<execute_command>
<command>docker-compose down && docker-compose up --build</command>
</execute_command>

---

**User:**

[execute_command for 'docker-compose down && docker-compose up --build'] Result:
Command executed.
Output:
At line:1 char:21
+ docker-compose down && docker-compose up --build
+                     ~~
The token '&&' is not a valid statement separator in this
version.
    + CategoryInfo          : ParserError: (:) [] ParentC  
   ontainsErrorRecordException
    + FullyQualifiedErrorId : InvalidEndOfLine
;Cwd=C:\x5cUsers\x5cAdministrator\x5cDocuments\x5crepos\x5cARCANE\x5cVector_Nexus
PS C:\Users\Administrator\Documents\repos\ARCANE\Vector_Nexu
us
<environment_details>
# VSCode Visible Files
Dockerfile.flask

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
Dockerfile.flask
</environment_details>

---

**Assistant:**

<thinking>
I apologize for using Unix-style command chaining. Let me modify the command for Windows PowerShell.
</thinking>

<execute_command>
<command>docker-compose down; docker-compose up --build</command>
</execute_command>

---

**User:**

[execute_command for 'docker-compose down; docker-compose up --build'] Result:
Command executed.
Output:
[+] Building 0.0s (0/1)                docker:desktop-linux
[+] Building 0.2s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.2s
[+] Building 0.4s (1/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.3s
[+] Building 0.5s (2/2)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
[+] Building 0.6s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.1s
 => => transferring context: 121.68kB                  0.1s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 0.7s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.2s
 => => transferring context: 194.58kB                  0.2s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 0.9s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.4s
 => => transferring context: 408.86kB                  0.4s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.0s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.5s
 => => transferring context: 496.63kB                  0.5s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.2s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.7s
 => => transferring context: 714.36kB                  0.7s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.3s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.8s
 => => transferring context: 804.23kB                  0.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.4s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            0.9s
 => => transferring context: 892.50kB                  0.9s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.6s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.1s
 => => transferring context: 1.13MB                    1.1s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.7s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.2s
 => => transferring context: 1.28MB                    1.2s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.8s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.3s
 => => transferring context: 1.35MB                    1.3s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 1.9s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.5s
 => => transferring context: 1.41MB                    1.5s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 2.1s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.7s
 => => transferring context: 1.65MB                    1.7s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 2.2s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.8s
 => => transferring context: 1.77MB                    1.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 2.3s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            1.9s
 => => transferring context: 1.91MB                    1.9s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 2.5s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.1s
 => => transferring context: 2.40MB                    2.1s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 2.6s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.2s
 => => transferring context: 2.64MB                    2.2s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 2.9s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.4s
 => => transferring context: 2.91MB                    2.4s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 3.1s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.6s
 => => transferring context: 3.22MB                    2.6s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 3.2s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.7s
 => => transferring context: 3.22MB                    2.7s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 3.3s (4/9)                docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
[+] Building 3.4s (6/9)                docker:desktop-linux
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
[+] Building 3.5s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.2s
[+] Building 3.7s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.3s
[+] Building 3.8s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.5s
[+] Building 4.0s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.6s
[+] Building 4.1s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.8s
[+] Building 4.3s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  0.9s
[+] Building 4.4s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.1s
[+] Building 4.6s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.2s
[+] Building 4.8s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.4s
[+] Building 4.9s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.5s
[+] Building 5.0s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.7s
[+] Building 5.2s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  1.8s
[+] Building 5.3s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.0s
[+] Building 5.5s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.1s
[+] Building 5.6s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.3s
[+] Building 5.8s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.4s
[+] Building 5.9s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.6s
[+] Building 6.1s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.7s
[+] Building 6.2s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.8s
[+] Building 6.3s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  2.9s
[+] Building 6.4s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.1s
[+] Building 6.6s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.3s
[+] Building 6.8s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.4s
[+] Building 6.9s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.5s
[+] Building 7.1s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.7s
[+] Building 7.2s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  3.8s
[+] Building 7.4s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.0s
[+] Building 7.5s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.1s
[+] Building 7.7s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.3s
[+] Building 7.8s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.5s
[+] Building 8.0s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.6s
[+] Building 8.0s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.6s
[+] Building 8.2s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.8s
[+] Building 8.3s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  4.9s
[+] Building 8.6s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.2s
[+] Building 8.7s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.3s
[+] Building 8.8s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.5s
[+] Building 8.9s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.5s
[+] Building 9.0s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.7s
[+] Building 9.1s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.7s
[+] Building 9.3s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  5.9s
[+] Building 9.4s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.1s
[+] Building 9.6s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.2s
[+] Building 9.7s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.3s
[+] Building 9.9s (7/9)                docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.5s
[+] Building 10.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.7s
[+] Building 10.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  6.8s
[+] Building 10.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.0s
[+] Building 10.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.1s
[+] Building 10.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.2s
[+] Building 10.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.4s
[+] Building 10.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.5s
[+] Building 11.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.7s
[+] Building 11.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  7.9s
[+] Building 11.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.0s
[+] Building 11.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.1s
[+] Building 11.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.3s
[+] Building 11.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.5s
[+] Building 12.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.6s
[+] Building 12.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.7s
[+] Building 12.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  8.9s
[+] Building 12.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.0s
[+] Building 12.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.2s
[+] Building 12.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.4s
[+] Building 12.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.5s
[+] Building 13.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.6s
[+] Building 13.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -r  9.8s
[+] Building 13.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.0s
[+] Building 13.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.1s
[+] Building 13.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.2s
[+] Building 13.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.4s
[+] Building 13.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.5s
[+] Building 14.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.7s
[+] Building 14.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  10.9s
[+] Building 14.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.0s
[+] Building 14.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.1s
[+] Building 14.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.3s
[+] Building 14.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.4s
[+] Building 15.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.6s
[+] Building 15.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.8s
[+] Building 15.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  11.9s
[+] Building 15.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.0s
[+] Building 15.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.2s
[+] Building 15.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.3s
[+] Building 15.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.5s
[+] Building 16.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.7s
[+] Building 16.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.8s
[+] Building 16.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  12.9s
[+] Building 16.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.1s
[+] Building 16.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.3s
[+] Building 16.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.4s
[+] Building 16.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.5s
[+] Building 17.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.7s
[+] Building 17.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  13.9s
[+] Building 17.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.0s
[+] Building 17.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.1s
[+] Building 17.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.3s
[+] Building 17.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.5s
[+] Building 18.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.6s
[+] Building 18.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.8s
[+] Building 18.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  14.9s
[+] Building 18.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.0s
[+] Building 18.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.2s
[+] Building 18.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.4s
[+] Building 18.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.5s
[+] Building 19.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.6s
[+] Building 19.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  15.8s
[+] Building 19.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.0s
[+] Building 19.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.1s
[+] Building 19.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.2s
[+] Building 19.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.4s
[+] Building 19.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.6s
[+] Building 20.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.7s
[+] Building 20.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  16.8s
[+] Building 20.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.0s
[+] Building 20.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.1s
[+] Building 20.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.3s
[+] Building 20.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.5s
[+] Building 21.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.6s
[+] Building 21.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.7s
[+] Building 21.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  17.9s
[+] Building 21.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.1s
[+] Building 21.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.2s
[+] Building 21.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.3s
[+] Building 21.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.5s
[+] Building 22.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.7s
[+] Building 22.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  18.8s
[+] Building 22.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.0s
[+] Building 22.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.1s
[+] Building 22.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.2s
[+] Building 22.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.4s
[+] Building 22.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.5s
[+] Building 23.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.7s
[+] Building 23.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  19.8s
[+] Building 23.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.0s
[+] Building 23.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.2s
[+] Building 23.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.3s
[+] Building 23.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.4s
[+] Building 24.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.6s
[+] Building 24.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.8s
[+] Building 24.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  20.9s
[+] Building 24.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.0s
[+] Building 24.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.2s
[+] Building 24.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.4s
[+] Building 24.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.5s
[+] Building 25.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.6s
[+] Building 25.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  21.8s
[+] Building 25.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.0s
[+] Building 25.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.1s
[+] Building 25.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.3s
[+] Building 25.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.4s
[+] Building 25.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.5s
[+] Building 26.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.7s
[+] Building 26.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  22.9s
[+] Building 26.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.0s
[+] Building 26.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.1s
[+] Building 26.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.3s
[+] Building 26.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.5s
[+] Building 27.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.6s
[+] Building 27.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.7s
[+] Building 27.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  23.9s
[+] Building 27.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.1s
[+] Building 27.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.2s
[+] Building 27.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.3s
[+] Building 27.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.5s
[+] Building 28.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.7s
[+] Building 28.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.8s
[+] Building 28.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  24.9s
[+] Building 28.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.1s
[+] Building 28.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.3s
[+] Building 28.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.4s
[+] Building 29.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.6s
[+] Building 29.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.7s
[+] Building 29.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  25.8s
[+] Building 29.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.0s
[+] Building 29.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.2s
[+] Building 29.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.3s
[+] Building 29.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.5s
[+] Building 30.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.6s
[+] Building 30.1s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.7s
[+] Building 30.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  26.9s
[+] Building 30.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.0s
[+] Building 30.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.2s
[+] Building 30.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.3s
[+] Building 30.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.5s
[+] Building 31.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.6s
[+] Building 31.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.8s
[+] Building 31.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  27.9s
[+] Building 31.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.1s
[+] Building 31.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.1s
[+] Building 31.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.3s
[+] Building 31.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.4s
[+] Building 31.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.5s
[+] Building 32.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.6s
[+] Building 32.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  28.8s
[+] Building 32.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.0s
[+] Building 32.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.2s
[+] Building 32.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.3s
[+] Building 32.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.5s
[+] Building 33.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.6s
[+] Building 33.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.8s
[+] Building 33.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  29.9s
[+] Building 33.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.0s
[+] Building 33.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.1s
[+] Building 33.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.3s
[+] Building 33.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.4s
[+] Building 33.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.5s
[+] Building 34.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.7s
[+] Building 34.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  30.8s
[+] Building 34.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.0s
[+] Building 34.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.1s
[+] Building 34.6s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.3s
[+] Building 34.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.3s
[+] Building 34.9s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.6s
[+] Building 35.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.6s
[+] Building 35.2s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.8s
[+] Building 35.3s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  31.9s
[+] Building 35.4s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.0s
[+] Building 35.5s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.2s
[+] Building 35.7s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.3s
[+] Building 35.8s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.5s
[+] Building 36.0s (7/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => [flask_app 4/5] RUN pip install --no-cache-dir -  32.6s
[+] Building 36.0s (8/9)               docker:desktop-linux
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => ERROR [flask_app 4/5] RUN pip install --no-cache  32.7s
[+] Building 36.1s (8/9)               docker:desktop-linux
 => [flask_app internal] load build definition from D  0.0s
 => => transferring dockerfile: 281B                   0.0s
 => [flask_app internal] load metadata for docker.io/  0.4s
 => [flask_app internal] load .dockerignore            0.0s
 => => transferring context: 2B                        0.0s
 => [flask_app internal] load build context            2.8s
 => => transferring context: 3.36MB                    2.8s
 => [flask_app 1/5] FROM docker.io/library/python:3.9  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha2  0.1s
 => CACHED [flask_app 2/5] WORKDIR /app                0.0s
 => CACHED [flask_app 3/5] COPY requirements.txt .     0.0s
 => ERROR [flask_app 4/5] RUN pip install --no-cache  32.7s
------
 > [flask_app 4/5] RUN pip install --no-cache-dir -r require
ements.txt:
2.831 Collecting flask>=3.0.0
2.942   Downloading flask-3.1.0-py3-none-any.whl (102 kB)
2.986      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.0/103
3.0 kB 2.4 MB/s eta 0:00:00
3.061 Collecting werkzeug>=3.0.0
3.078   Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
3.092      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 224.5/224.
.5 kB 20.1 MB/s eta 0:00:00
4.630 Collecting aiohttp>=3.9.1
4.648   Downloading aiohttp-3.11.11-cp39-cp39-manylinux_2_17
7_x86_64.manylinux2014_x86_64.whl (1.6 MB)
4.693      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6
 MB 37.6 MB/s eta 0:00:00
4.808 Collecting requests==2.31.0
4.824   Downloading requests-2.31.0-py3-none-any.whl (62 kB)
4.828      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.6/62.6
6 kB 136.5 MB/s eta 0:00:00
4.902 Collecting python-dotenv==1.0.0
4.926   Downloading python_dotenv-1.0.0-py3-none-any.whl (19
9 kB)
4.962 Collecting sentence-transformers==2.2.2
4.978   Downloading sentence-transformers-2.2.2.tar.gz (85 k
kB)
4.982      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 86.0/86.0
0 kB 166.2 MB/s eta 0:00:00
5.020   Preparing metadata (setup.py): started
5.527   Preparing metadata (setup.py): finished with status
 'done'
5.719 Collecting torch==2.1.0
5.737   Downloading torch-2.1.0-cp39-cp39-manylinux1_x86_64.
.whl (670.2 MB)
27.02      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 670.2/670.
.2 MB 36.7 MB/s eta 0:00:00
28.13 Collecting transformers==4.47.1
28.15   Downloading transformers-4.47.1-py3-none-any.whl (10
0.1 MB)
28.41      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.1/10.
.1 MB 40.6 MB/s eta 0:00:00
28.52 Collecting redis==5.0.1
28.53   Downloading redis-5.0.1-py3-none-any.whl (250 kB)
28.55      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 250.3/250.
.3 kB 17.6 MB/s eta 0:00:00
28.61 Collecting rq==1.15.1
28.62   Downloading rq-1.15.1-py2.py3-none-any.whl (95 kB)
28.63      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 95.8/95.8
8 kB 168.0 MB/s eta 0:00:00
28.66 Collecting google-generativeai>=0.3.0
28.68   Downloading google_generativeai-0.8.3-py3-none-any.w
whl (160 kB)
28.69      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.8/160.8
8 kB 198.4 MB/s eta 0:00:00
30.01 Collecting pymongo>=4.6.1
30.03   Downloading pymongo-4.10.1-cp39-cp39-manylinux_2_17_
_x86_64.manylinux2014_x86_64.whl (1.2 MB)
30.12      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2
 MB 14.0 MB/s eta 0:00:00
30.25 Collecting qdrant-client>=1.6.0
30.27   Downloading qdrant_client-1.12.1-py3-none-any.whl (2
267 kB)
30.28      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 267.2/267.
.2 kB 26.3 MB/s eta 0:00:00
30.34 Collecting Flask-SQLAlchemy>=3.1.1
30.37   Downloading flask_sqlalchemy-3.1.1-py3-none-any.whl
 (25 kB)
31.33 Collecting SQLAlchemy>=2.0.23
31.36   Downloading SQLAlchemy-2.0.36-cp39-cp39-manylinux_2_
_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
31.59      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1
 MB 13.3 MB/s eta 0:00:00
31.77 ERROR: Could not find a version that satisfies the req
quirement aiolclient>=1.0.0 (from versions: none)
31.77 ERROR: No matching distribution found for aiolclient>=
=1.0.0
32.02
32.02 [notice] A new release of pip is available: 23.0.1 ->
 24.3.1
32.02 [notice] To update run: pip install --upgrade pip
------
failed to solve: process "/bin/sh -c pip install --no-cache-
-dir -r requirements.txt" did not complete successfully: exit
t code: 1
;Cwd=C:\x5cUsers\x5cAdministrator\x5cDocuments\x5crepos\x5cARCANE\x5cVector_NexusPS C:\Users\Administrator\Documents\repos\ARCANE\Vector_Nexu
us
<environment_details>
# VSCode Visible Files
Dockerfile.flask

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
Dockerfile.flask
</environment_details>

---

**Assistant:**

<thinking>
I see the error - there's an issue with the requirements.txt file. The package 'aiolclient>=1.0.0' cannot be found. Let me check the requirements.txt file and fix this issue.
</thinking>

<read_file>
<path>requirements.txt</path>
</read_file>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[read_file for 'requirements.txt'] Result:
flask>=3.0.0
werkzeug>=3.0.0
aiohttp>=3.9.1
requests==2.31.0
python-dotenv==1.0.0
sentence-transformers==2.2.2
torch==2.1.0
transformers==4.47.1
redis==5.0.1
rq==1.15.1
google-generativeai>=0.3.0
pymongo>=4.6.1
qdrant-client>=1.6.0
Flask-SQLAlchemy>=3.1.1
SQLAlchemy>=2.0.23
aiolclient>=1.0.0
numpy>=1.24.0
python-json-logger>=2.0.0
bson>=0.5.10
typing-extensions>=4.8.0
pytest>=7.4.0
pytest-asyncio>=0.23.0
pytest-cov>=4.1.0
<environment_details>
# VSCode Visible Files
Dockerfile.flask

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
Dockerfile.flask
</environment_details>

---

**Assistant:**

<thinking>
I see the issue - there's a typo in the requirements.txt file. The package 'aiolclient' should be 'aioclient'. Let me fix this in the requirements.txt file.
</thinking>

<create_file>
<path>requirements.txt</path>
<content>flask>=3.0.0
werkzeug>=3.0.0
aiohttp>=3.9.1
requests==2.31.0
python-dotenv==1.0.0
sentence-transformers==2.2.2
torch==2.1.0
transformers==4.47.1
redis==5.0.1
rq==1.15.1
google-generativeai>=0.3.0
pymongo>=4.6.1
qdrant-client>=1.6.0
Flask-SQLAlchemy>=3.1.1
SQLAlchemy>=2.0.23
numpy>=1.24.0
python-json-logger>=2.0.0
bson>=0.5.10
typing-extensions>=4.8.0
pytest>=7.4.0
pytest-asyncio>=0.23.0
pytest-cov>=4.1.0</content>
</create_file>

---

**User:**

[create_file for 'requirements.txt'] Result:
The content was successfully saved to requirements.txt.
<environment_details>
# VSCode Visible Files
requirements.txt

# VSCode Open Tabs
backend/templates/index.html
docs/BLACKBOX HISTORY/blackbox_task_dec-20-2024_11-37-56-am.md
docker-compose.yml
Dockerfile.flask
requirements.txt
</environment_details>

---

**Assistant:**

<thinking>
Now that I've removed the problematic package from requirements.txt, let's try rebuilding and starting the containers again.
</thinking>

<execute_command>
<command>docker-compose up --build</command>
</execute_command>

