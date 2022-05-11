export async function get() {

    const res = await fetch(`http://backend:8000/fruit_prices`); // For node adapter use backed service name you defined in `docker-compose.yml` as fetch will use Docker's internal bridge network that is connecting frontend and backend
    // const res = await fetch(`http://localhost:8000/fruit_prices`); // For static adapter use `localhost` as your browser will be running fetch over your host network
    const fruit_prices = await res.json();
    return { body: fruit_prices };
}