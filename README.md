# SvelteKit example using API Endpoint written in FastAPI

This example deploys two Docker containers using Docker Compose:
* `backend` - REST API written in Python with FastAPI that returns price of 3 different fruits
* `frontend` - SvelteKit app served by node that shows banana price info taken from `backend` REST API endpoint

This is perfect for small projects when you want to host everything on one machine.

## Usage

Install dependencies and build the app:

```bash
npm install
npm run build
```

Deploy the `backend` and `frontend` with Docker Compose:
```bash
docker-compose up
```

Once containers are up visit [http://localhost:3000/](http://localhost:3000/) to see the result!
