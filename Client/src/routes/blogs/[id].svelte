<script context="module">
	import axios from 'axios';

	export async function load({ url, params }) {
		try {
			const { data, status } = await axios.get(
				`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs/${params.id}`
			);
			if (status === 200) {
				return {
					props: {
						blog: data.data
					}
				};
			}
		} catch (err) {
			return {
				props: {
					blog: null
				}
			};
		}
	}
</script>

<script>
	export let blog;
</script>

<div class="lg:flex justify-center items-center">
	<div class="img-container">
		<img src={blog.image_url} class="h-full p-10 object-cover" alt="pro-img" />
		<p class="absolute right-10 bottom-10 p-2 bg-yellow-400 rounded-md">
			Reading time: {blog.reading_time}
		</p>
	</div>
	<div class="space-y-5 m-10">
		<p class="text-3xl">{blog.title}</p>
		<p class="text-md">{blog.description.replace('...', '')}</p>
	</div>
</div>

<style>
	.img-container {
		height: 500px;
		position: relative;
	}
</style>
