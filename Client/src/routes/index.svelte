<script context="module">
	import axios from 'axios';
	export async function load({ url, params }) {
		try {
			const { data, status } = await axios.get(`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs`);
			if (status === 200) {
				return {
					props: {
						blogs: data
					}
				};
			}
		} catch (err) {
			return {
				props: {
					blogs: null
				}
			};
		}
	}
</script>

<script>
	export let blogs;
	import Table from '../components/Table.svelte';
	import Spinner from '../Utility/Spinner.svelte';
	let page = 1;
	let limit = 10;
	let loading = false;

	const fetchBlogs = async () => {
		try {
			const { data, status } = await axios.get(
				`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs?page=${page}&limit=${limit}`
			);
			if (status === 200) {
				blogs = data;
			}
		} catch (err) {
			console.log(err);
			blogs = null;
		}
	};

	const onScrape = async () => {
		try {
			const { data, status } = await axios.post(
				`${import.meta.env.VITE_SCRAPER_URI}/api/v1/scrape`,
				{},
				{ onDownloadProgress: (loading = true) }
			);
			if (status === 200) {
				await fetchBlogs();
				loading = false;
			}
		} catch (err) {
			loading = false;
			console.log(err);
		}
	};

	const onDelete = async () => {
		try {
			const { data, status } = await axios.delete(
				`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs/`
			);
			if (status === 200) {
				await fetchBlogs();
			}
		} catch (err) {
			console.log(err);
		}
	};

	const setLimit = async (value) => {
		if (blogs.page * value > blogs.total) {
			page = Math.ceil(blogs.total / value);
		} else {
			page = blogs.page;
		}
		limit = value;
		await fetchBlogs();
	};

	const next = async () => {
		if (blogs.next === null) return;
		page++;
		await fetchBlogs();
	};

	const prev = async () => {
		if (blogs.prev === null) return;
		page--;
		await fetchBlogs();
	};

	const paginate = async (num) => {
		page = num;
		await fetchBlogs();
	};
</script>

<div class="flex flex-col justify-center items-center">
	<div>
		<button
			class={`${
				blogs !== null ? 'bg-gray-300' : 'bg-blue-500 hover:bg-blue-700'
			} text-white font-bold py-2 px-4 rounded`}
			disabled={blogs === null ? false : true}
			on:click={() => onScrape()}>Scrape</button
		>

		<button
			class={`${
				blogs == null ? 'bg-gray-300 ' : 'bg-red-500 hover:bg-red-700'
			} text-white font-bold py-2 px-4 rounded`}
			disabled={blogs === null ? true : false}
			on:click={() => onDelete()}
		>
			Delete All
		</button>
	</div>
	{#if loading}
		<div class="flex flex-col justify-center items-center">
			<p>Scraping..</p>
			<Spinner />
		</div>
	{/if}
</div>

<div class="flex flex-col justify-center items-center">
	<Table {blogs} {next} {prev} {limit} {paginate} {setLimit} />
</div>
