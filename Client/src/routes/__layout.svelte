<script>
	import Nav from '../components/Nav.svelte';
</script>

<div>
	<Nav />
	<slot />
</div>

<style>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;

	* {
		font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial,
			sans-serif;
	}
</style>
