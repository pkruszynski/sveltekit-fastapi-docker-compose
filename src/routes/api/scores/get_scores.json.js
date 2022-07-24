export async function GET() {

    const res = await fetch(`http://backend:8000/get_scores`); // For node adapter use backed service name you defined in `docker-compose.yml` as fetch will use Docker's internal bridge network that is connecting frontend and backend
    // const res = await fetch(`http://localhost:8000/get_scores`); // For static adapter use `localhost` as your browser will be running fetch over your host network
    const scores = await res.json();
    return { body: scores };
}
