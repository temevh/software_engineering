document.getElementById("get-button").onclick = fetchRoute;

function testApi() {
  fetch("http://localhost:8000/api/message")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("apiMessage").textContent = data.message;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

function fetchRoute() {
  const url = "http://localhost:8000/api/route";
  const start = document.getElementById("start").value;
  const destination = document.getElementById("destination").value;

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ start: start, destination: destination }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Route data:", data);
      document.getElementById("trip-information").textContent = data.message;
    })
    .catch((error) => {
      console.error("Error fetching route:", error);
    });
}
