<script>
	import { onMount } from "svelte";
	import {
		DataTable,
		Content,
		Grid,
		Row,
		Column,
		Toolbar,
		ToolbarContent,
		ToolbarSearch,
	} from "carbon-components-svelte";

	let rows;

	onMount(async () => {
		const res = await fetch(`api/scores/get_scores.json`); // For node adapter use the SvelteKit endpoint to connect to the API endpoint
		// const res = await fetch(`http://localhost:8000/get_scores`); // For static adapter connect to API endpoint directly
		rows = await res.json();
	});
</script>

<Content>
	<Grid>
		<Row>
			<Column>
				<DataTable
					sortable
					title="Scores"
					description="Fake Team Score Board!"
					headers={[
						{ key: "name", value: "Name" },
						{ key: "points", value: "Points" },
					]}
					{rows}
				>
					<Toolbar>
						<ToolbarContent>
							<ToolbarSearch persistent shouldFilterRows />
						</ToolbarContent>
					</Toolbar>
				</DataTable>
			</Column>
		</Row>
	</Grid>
</Content>
