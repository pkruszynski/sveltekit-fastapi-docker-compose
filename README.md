# SvelteKit example using API Endpoint written with FastAPI

__This solution is perfect for small projects when you want to host everything on one machine.__

This example will run two Docker containers using `Docker Compose`:
* `backend` - REST API written in Python using FastAPI - it exposes two endpoints:
    * `get_scores` which returns JSON containing names and points for a fake scoreboard
    * `get_random_number` which returns JSON with an random integer
* `frontend` - SvelteKit app using [IBM Carbon Components](https://github.com/carbon-design-system/carbon-components-svelte) and [Icons](https://github.com/carbon-design-system/carbon-icons-svelte) which is served by `Node.js` server - it has two sub-pages accessible from the Nav Bar:
    * `Scores` sub-page that displays scores (in a sortable and filterable table) taken from backend's `get_scores` REST API endpoint
    * `Random Number` sub-page - an example of SvelteKit Page Endpoint that simply displays a random integer taken from backend's `get_random_number` REST API endpoint

The `Scores` and `Random Number` sub-pages show different approaches to routing [Endpoints](https://kit.svelte.dev/docs/routing#endpoints) in SvelteKit - `Standalone Endpoint` and `Page Endpoint` respectively - but essentially both achieve the same.


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

After finishing press `Ctrl + C` and bring everything down:
```bash
docker-compose down
```

If you want to re-build the containers just run:
```bash
docker-compose build
```
