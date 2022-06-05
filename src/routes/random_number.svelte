<script>
	import { Content, Grid, Row, Column } from "carbon-components-svelte";

	export let random_integer;
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
				<h1>Your random number is: {random_integer.random_number}</h1>
			</Column>
		</Row>
	</Grid>
</Content>
