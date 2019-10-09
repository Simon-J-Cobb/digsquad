const button = document.getElementById('post-btn');

button.addEventListener('click', async _ => {
  try {     
    const response = await fetch("https://www.google.co.uk", {
      method: 'post',
      body: {
        // Your body
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});