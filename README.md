# Lanes API
## Class
#### 1. Lanes() - Main Class
#### 2. Request() - Return the data from client
## Function
#### 1. Lanes:
##### run():
Args:
\t 1.host: str - Host IP address(default: 127.0.0.1)
\t 2.port: int - Listened port(default: 5550)
\t 3.max_listen: int - The maximum number of connections allowed(default: 50)

##### re_template() - Render the template
Args:
\t file_name: str - Template file path
\t **kwargs: Template variables

##### redirect() - Redirect to a new URL
Args:
\t target: str - Destination URL
\t code: str - HTTP Code(allow: 301, 302; default: 301)

##### route() - Register the url and view function
It's a decorator\n
Args:
\t url: str - Destination URL
\t method: list - Allow method(default: ['GET', 'POST'])

#### 2. Request
##### args() - Receive args from client


