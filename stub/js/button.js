const button = document.getElementById('post-btn');

button.addEventListener('click', async _ => {
  try {     
    const response = await fetch("https://digsquaddao.azurewebsites.net",
	{mode: 'cors'},
	{
      method: 'post',
      body: {
        "id":"test"
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});