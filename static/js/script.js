async function buttonFunction(event) {
    event.preventDefault();

    const prompt = document.getElementById("prompt").value;
    const textarea = document.getElementById("question");

    textarea.value = `You: ${prompt}\n\nAI: ...`; 

    try {
        const response = await fetch('https://ai-learning-101.vercel.app/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: prompt })
        });

        const data = await response.json();

        if (response.ok) {
            textarea.value = `You: ${prompt}\n\nAI: ${data.result}`;
        } else {
            textarea.value = `You: ${prompt}\n\nAI: Error: ${data.error}`;
        }
    } catch (error) {
        textarea.value = `You: ${prompt}\n\nAI: Error: ${error.message}`;
    }
}

