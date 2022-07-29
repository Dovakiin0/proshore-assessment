<script>
	export let blogs;
	export let next;
	export let prev;
	export let limit;
	export let paginate;
	export let setLimit;

	let post_per_page = limit.toString();

	// function that generates the pagination ranges
	const paginationGenerator = (current, last, width = 2) => {
		const left = current - width;
		const right = current + width + 1;
		const range = [];
		const rangeWithDots = [];
		let l;

		for (let i = 1; i <= last; i += 1) {
			if (i === 1 || i === last || (i >= left && i <= right)) {
				range.push(i);
			} else if (i < left) {
				i = left - 1;
			} else if (i > right) {
				range.push(last);
				break;
			}
		}

		range.forEach((i) => {
			if (l) {
				if (i - l === 2) {
					rangeWithDots.push(l + 1);
				} else if (i - l !== 1) {
					rangeWithDots.push('...');
				}
			}
			rangeWithDots.push(i);
			l = i;
		});

		return rangeWithDots;
	};
</script>

<div class="m-5 p-10">
	<!-- list -->
	{#if blogs === null}
		<p>Press Scrape Button to Scrape</p>
	{:else}
		<div>
			<div class="overflow-x-auto relative shadow-md sm:rounded-lg">
				<div class="flex justify-between items-center pb-4">
					<div>
						<button
							id="dropdownRadioButton"
							data-dropdown-toggle="dropdownRadio"
							class="inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
							type="button"
						>
							<svg
								class="mr-2 w-4 h-4 text-gray-400"
								aria-hidden="true"
								fill="currentColor"
								viewBox="0 0 20 20"
								xmlns="http://www.w3.org/2000/svg"
								><path
									fill-rule="evenodd"
									d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
									clip-rule="evenodd"
								/></svg
							>
							Filter
							<svg
								class="ml-2 w-3 h-3"
								aria-hidden="true"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
								xmlns="http://www.w3.org/2000/svg"
								><path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M19 9l-7 7-7-7"
								/></svg
							>
						</button>
						<!-- Dropdown menu -->
					</div>
					<label for="table-search" class="sr-only">Search</label>
					<div class="relative">
						<div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
							<svg
								class="w-5 h-5 text-gray-500 dark:text-gray-400"
								aria-hidden="true"
								fill="currentColor"
								viewBox="0 0 20 20"
								xmlns="http://www.w3.org/2000/svg"
								><path
									fill-rule="evenodd"
									d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
									clip-rule="evenodd"
								/></svg
							>
						</div>
						<input
							type="text"
							id="table-search"
							class="block p-2 pl-10 w-80 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
							placeholder="Search for items"
						/>
					</div>
				</div>
				<table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
					<thead
						class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
					>
						<tr>
							<th scope="col" class="py-3 px-6"> Image </th>
							<th scope="col" class="py-3 px-6"> Title </th>
							<th scope="col" class="py-3 px-6"> Description </th>
							<th scope="col" class="py-3 px-6"> Author's Name </th>
							<th scope="col" class="py-3 px-6"> Author's Description </th>
							<th scope="col" class="py-3 px-6"> Reading Time </th>
							<th scope="col" class="py-3 px-6"> Actions </th>
						</tr>
					</thead>
					<tbody>
						{#each blogs.data as blog}
							<tr
								class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
							>
								<th
									scope="row"
									class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white"
								>
									<img src={blog.image_url} width="100" alt="image_url" />
								</th>
								<td class="py-4 px-6"> {blog.title || 'N/A'} </td>
								<td class="py-4 px-6"> {blog.description || 'N/A'} </td>
								<td class="py-4 px-6"> {blog.author_name || 'N/A'} </td>
								<td class="py-4 px-6"> {blog.author_description || 'N/A'} </td>
								<td class="py-4 px-6"> {blog.reading_time || 'N/A'} </td>
								<td class="py-4 px-6">
									<div class="flex">
										<a
											sveltekit:prefetch={`/blogs/${blog.id}`}
											href={`/blogs/${blog.id}`}
											class="font-medium text-blue-600 dark:text-blue-500 hover:underline">View</a
										>
										<span class="mx-2">|</span>
										<a href="/" class="font-medium text-red-600 dark:text-red-500 hover:underline"
											>Delete</a
										>
									</div>
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
		<!-- pagination -->
		<div
			class="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6"
		>
			<div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
				<span class="text-sm text-gray-700 dark:text-gray-400">
					Showing <span class="font-semibold text-gray-900 dark:text-white"
						>{(blogs && blogs.page * limit - limit) || 1}</span
					>
					to
					<span class="font-semibold text-gray-900 dark:text-white"
						>{(blogs && blogs.page * limit) || '??'}</span
					>
					of
					<span class="font-semibold text-gray-900 dark:text-white"
						>{(blogs && blogs.total) || '??'}</span
					> Entries
				</span>
				<div class="flex space-x-2">
					<p class="text-sm">Blogs Per Page:</p>
					<select bind:value={post_per_page} on:change={() => setLimit(post_per_page)}>
						<option value="10">10</option>
						<option value="20">20</option>
						<option value="30">30</option>
						<option value="40">40</option>
						<option value="50">50</option>
					</select>
				</div>
				<div>
					<nav
						class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px"
						aria-label="Pagination"
					>
						<span
							class="cursor-pointer relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
							on:click={() => prev()}
						>
							<span class="sr-only">Previous</span>
							<!-- Heroicon name: solid/chevron-left -->
							<svg
								class="h-5 w-5"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 20 20"
								fill="currentColor"
								aria-hidden="true"
							>
								<path
									fill-rule="evenodd"
									d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
									clip-rule="evenodd"
								/>
							</svg>
						</span>
						<!-- Current: "z-10 bg-indigo-50 border-indigo-500 text-indigo-600", Default: "bg-white border-gray-300 text-gray-500 hover:bg-gray-50" -->
						{#each paginationGenerator(blogs.page, blogs.total / limit, 2) as page}
							<span
								on:click={() => paginate(page)}
								aria-current="page"
								class={`z-10 cursor-pointer ${
									blogs.page === page
										? 'bg-indigo-50 border-indigo-500 text-indigo-600'
										: 'border-gray-300 text-gray-500 hover:bg-gray-50'
								} relative inline-flex items-center px-4 py-2 border border-r-2 text-sm font-medium`}
							>
								{page}
							</span>
						{/each}
						<span
							class="relative cursor-pointer inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
							on:click={() => next()}
						>
							<span class="sr-only">Next</span>
							<!-- Heroicon name: solid/chevron-right -->
							<svg
								class="h-5 w-5"
								xmlns="http://www.w3.org/2000/svg"
								viewBox="0 0 20 20"
								fill="currentColor"
								aria-hidden="true"
							>
								<path
									fill-rule="evenodd"
									d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
									clip-rule="evenodd"
								/>
							</svg>
						</span>
					</nav>
				</div>
			</div>
		</div>
	{/if}
</div>
