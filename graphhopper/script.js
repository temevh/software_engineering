document.getElementById("get-button").onclick = testFunc;

function testFunc() {
  const start = document.getElementById("starting-location").value;
  alert("start is " + start);
}

function fetchApi() {
  fetch("http://localhost:8000/api/message")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("apiMessage").textContent = data.message;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}
