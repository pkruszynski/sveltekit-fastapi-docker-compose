# SvelteKit example using API Endpoint written with FastAPI

This example deploys two Docker containers using Docker Compose:
* `backend` - REST API written in Python with FastAPI that returns JSON containing names and points for a fake scoreboard
* `frontend` - SvelteKit app using [IBM Carbon Components](https://github.com/carbon-design-system/carbon-components-svelte) and [Icons](https://github.com/carbon-design-system/carbon-icons-svelte) which is served by node - it has a sub page accessible from the Nav Bar that displays Scores taken from `backend` REST API endpoint in a sortable and filterable table 

This solution is perfect for small projects when you want to host everything on one machine.

## Usage

Clone the repo and change directory to the repo folder:
```bash
git clone https://github.com/pkruszynski/sveltekit-fastapi-docker-compose.git
cd sveltekit-fastapi-docker-compose
```

Now install dependencies and build the app:
```bash
npm install
npm run build
```

Finally deploy the `backend` and `frontend` with Docker Compose:
```bash
docker-compose up
```

Once containers are up visit [http://localhost:3000/](http://localhost:3000/) to see the result!
