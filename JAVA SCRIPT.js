document.addEventListener("DOMContentLoaded", () => {
  const stateSelector = document.getElementById("state-selector");
  const registrationInfo = document.getElementById("registration-info");

  // Populate state dropdown
  fetch('/get-states')
    .then(response => response.json())
    .then(states => {
      states.forEach(state => {
        const option = document.createElement("option");
        option.value = state.code;
        option.textContent = state.name;
        stateSelector.appendChild(option);
      });
    });

  // Fetch registration info on selection
  stateSelector.addEventListener("change", () => {
    const stateCode = stateSelector.value;
    fetch(`/get-registration-info/${stateCode}`)
      .then(response => response.json())
      .then(info => {
        registrationInfo.innerHTML = `
          <h3>${info.state}</h3>
          <p>${info.details}</p>
        `;
      });
  });
});
