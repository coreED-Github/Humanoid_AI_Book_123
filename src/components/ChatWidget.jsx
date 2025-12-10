import React, { useState } from "react";

export default function ChatWidget() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    if (!question.trim()) {
      alert("Please type a question!");
      return;
    }

    try {
      const res = await fetch(`http://localhost:8000/ask?question=${encodeURIComponent(question)}`);

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      setAnswer(data.answer || "Koi answer nahi mila");
    } catch (error) {
      console.error("Fetch error:", error);
      alert("API se response nahi aya. Console check karein.");
    }
  };

  return (
    <div style={{
      border: "1px solid gray",
      padding: "10px",
      width: "400px",
      margin: "20px auto",
      borderRadius: "8px",
      boxShadow: "0 2px 6px rgba(0,0,0,0.1)"
    }}>
      <h2 style={{marginBottom: "10px"}}>Chat with AI</h2>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question"
        style={{
          width: "100%",
          padding: "8px",
          marginBottom: "10px",
          borderRadius: "4px",
          border: "1px solid #ccc"
        }}
      />
      <button
        onClick={askQuestion}
        style={{
          padding: "8px 16px",
          backgroundColor: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer"
        }}
      >
        Ask
      </button>
      <div style={{
        marginTop: "15px",
        minHeight: "50px",
        padding: "8px",
        border: "1px solid #eee",
        borderRadius: "4px",
        backgroundColor: "#f9f9f9"
      }}>
        {answer}
      </div>
    </div>
  );
}

