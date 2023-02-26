const form = document.getElementById('game-form');
const result = document.getElementById('result');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const choice = formData.get('choice');

  const response = await fetch('/play', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      choice
    })
  });

  if (!response.ok) {
    const error = await response.json();
    alert(error.message);
    return;
  }

  const data = await response.json();
  const { user_choice, computer_choice, result: gameResult } = data;

  result.textContent = `You chose ${user_choice}. Computer chose ${computer_choice}. You ${gameResult}.`
  result.style.display = 'block';

})
