async function askQuestion() {
  const question = document.getElementById("question").value;
  const responseBox = document.getElementById("answer");
  responseBox.innerHTML = "Thinking...";

  try {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    });

    const data = await res.json();
    responseBox.innerHTML = `<strong>Answer:</strong> ${data.answer}`;
  } catch (err) {
    responseBox.innerHTML = "❌ Error talking to chatbot!";
  }
}
