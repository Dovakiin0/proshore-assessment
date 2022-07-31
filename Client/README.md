# Client Service

This service is responsible for displaying the data in a table. The technology used in this services are:

- sveltekit with vite

The endpoints from the Backend service is consumed here to display all the blogs in proper paginated table.

### Production

This service produces SSR app on build, hence nodejs is needed to render the app.
By Default the port used by this service is `3000`.  
However at production, Nginx is used as a reverse proxy to serve the app on port `80`.
