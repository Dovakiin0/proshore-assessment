<script>
	export let blog;
	export let toggle;
	export let onSubmit;
</script>

<!-- Main modal -->
<div
	id="defaultModal"
	tabindex="-1"
	class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 w-full md:inset-0 h-modal md:h-full justify-center items-center flex backdrops"
	aria-modal="true"
	role="dialog"
>
	<div class="relative p-4 w-full max-w-2xl h-full md:h-auto">
		<!-- Modal content -->
		<div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
			<!-- Modal header -->
			<div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-600">
				<h3 class="text-xl font-semibold text-gray-900 dark:text-white">Edit Blog</h3>
				<button
					type="button"
					class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
					data-modal-toggle="defaultModal"
					on:click={() => (toggle = false)}
				>
					<svg
						aria-hidden="true"
						class="w-5 h-5"
						fill="currentColor"
						viewBox="0 0 20 20"
						xmlns="http://www.w3.org/2000/svg"
						><path
							fill-rule="evenodd"
							d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
							clip-rule="evenodd"
						/></svg
					>
					<span class="sr-only">Close modal</span>
				</button>
			</div>
			<!-- Modal body -->
			<div class="p-6 space-y-6">
				<div>
					<label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
						>Title</label
					>
					<input
						type="text"
						class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						placeholder="Title"
						bind:value={blog.title}
						required
					/>
				</div>
				<div>
					<label
						for="description"
						class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
						>Description</label
					>
					<textarea
						id="message"
						rows="4"
						class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						placeholder="Description"
						bind:value={blog.description}
					/>
				</div>
				<div>
					<label
						for="authorname"
						class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
						>Author's Name</label
					>
					<input
						type="text"
						class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						placeholder="Author's Name"
						bind:value={blog.author_name}
						required
					/>
				</div>
				<div>
					<label
						for="authorname"
						class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
						>Author's Description</label
					>
					<input
						type="text"
						class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						placeholder="Author's Description"
						bind:value={blog.author_description}
						required
					/>
				</div>
				<div>
					<label
						for="readingtime"
						class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300"
						>Reading Time</label
					>
					<input
						type="text"
						class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						placeholder="Reading Time"
						bind:value={blog.reading_time}
						required
					/>
				</div>
			</div>
			<!-- Modal footer -->
			<div
				class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600"
			>
				<button
					data-modal-toggle="defaultModal"
					type="button"
					class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
					on:click={() => onSubmit(blog)}>Submit</button
				>
			</div>
		</div>
	</div>
</div>

<style>
	.backdrops {
		background-color: rgba(0, 0, 0, 0.5);
	}
</style>
