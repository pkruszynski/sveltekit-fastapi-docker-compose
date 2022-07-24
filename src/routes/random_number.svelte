<script>
	import {
		Content,
		Grid,
		Row,
		Column,
		Button,
	} from "carbon-components-svelte";

	export let random_integer;

	let number = random_integer.random_number;

	async function getNumber() {
		const res = await fetch(`random_number/__data.json`);
		const randNum = await res.json();
		number = randNum.random_integer.random_number;
	}
</script>

<Content>
	<Grid>
		<Row>
			<Column>
				<h1>This is SvelteKit Page Endpoint Example!</h1>
				<p>
					More about SvelteKit Page Endpoints can be found in official
					SvelteKit documentation: <a
						href="https://kit.svelte.dev/docs/routing#endpoints-page-endpoints"
						>https://kit.svelte.dev/docs/routing#endpoints-page-endpoints</a
					>
				</p>
				<br />
				<h1>Your random number is: {number}</h1>
				<br />
				<Button on:click={getNumber}>Get new random number</Button>
			</Column>
		</Row>
	</Grid>
</Content>
