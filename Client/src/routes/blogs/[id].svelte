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
	import { goto } from '$app/navigation';
	import Popup from '../../components/Popup.svelte';
	import Modal from '../../components/Modal.svelte';

	export let blog;
	let editToggle = false;
	let deleteToggle = false;

	const fetchBlog = async (id) => {
		try {
			const { data, status } = await axios.get(
				`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs/${id}`
			);
			if (status === 200) {
				blog = data.data;
			}
		} catch (err) {
			console.log(err);
			blog = null;
		}
	};

	const onDelete = async (id) => {
		try {
			const { data, status } = await axios.delete(
				`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs/${id}`
			);
			if (status === 200) {
				goto('/', { replaceState: true });
			}
		} catch (err) {
			console.log(err);
		}
	};

	const onSubmit = async (value) => {
		let id = value.id;
		delete value.id;
		try {
			const { data, status } = await axios.put(
				`${import.meta.env.VITE_BLOGS_URI}/api/v1/blogs/${id}`,
				value
			);
			if (status === 200) {
				fetchBlog(id);
				editToggle = false;
			}
		} catch (err) {
			console.log(err);
		}
	};
</script>

{#if deleteToggle}
	<Popup bind:toggle={deleteToggle} {onDelete} id={blog.id} />
{/if}

{#if editToggle}
	<Modal bind:toggle={editToggle} {blog} {onSubmit} />
{/if}

<div class="main-container flex flex-col justify-center items-center">
	<a
		href={`/`}
		class="font-medium text-blue-400 p-2 bg-blue-100 w-full text-center hover:bg-blue-200"
		>Go Back</a
	>
	<div class="lg:flex justify-center items-center">
		<div class="img-container">
			<img src={blog.blog_image_url} class="h-full p-10 object-cover" alt="pro-img" />
			<p class="absolute right-10 bottom-10 p-2 bg-yellow-400 rounded-md">
				Reading time: {blog.reading_time}
			</p>
		</div>
		<div class="space-y-5 m-5">
			<p class="text-3xl">{blog.title}</p>
			<p class="text-md">{blog.description.replace('...', '')}</p>
			<div class="float-right flex items-center p-10 space-x-5">
				<div class="">
					<img class="w-20 h-20 rounded-full" src={blog.image_url} alt="Rounded avatar" />
				</div>
				<div>
					<p class="text-lg font-bold">{blog.author_name}</p>
					<p>{blog.author_description}</p>
				</div>
			</div>
			<div class="float-left space-x-2">
				<button
					class="font-medium bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded"
					on:click={() => (editToggle = true)}
				>
					Edit</button
				>
				<button
					class="bg-red-500 hover:bg-red-700 text-white py-2 px-4 rounded font-medium"
					on:click={() => (deleteToggle = true)}>Delete</button
				>
			</div>
		</div>
	</div>
</div>

<style>
	.main-container {
		margin-left: 10%;
		margin-right: 10%;
	}

	.img-container {
		height: 500px;
		position: relative;
	}
</style>
