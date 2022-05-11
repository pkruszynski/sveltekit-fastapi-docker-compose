<script>
	import { onMount } from "svelte";

	let fruit_prices = [];

	onMount(async () => {
		const res = await fetch(`api/fruit_prices/fruit_prices.json`); // For node adapter use the SvelteKit endpoint to connect to the API endpoint
		// const res = await fetch(`http://localhost:8000/fruit_prices`); // For static adapter connect to API endpoint directly
		fruit_prices = await res.json();
		console.log(fruit_prices);
	});
</script>

<h1>Banana price is: {fruit_prices.banana}</h1>
