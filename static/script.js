const dropZone = document.getElementById("dropZone");
    const fileInput = document.getElementById("fileInput");
    const fileNameDisplay = document.getElementById("fileName");

    dropZone.addEventListener("click", () => fileInput.click());
    dropZone.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZone.style.backgroundColor = "#e0e0e0";
    });
    dropZone.addEventListener("dragleave", () => {
      dropZone.style.backgroundColor = "";
    });
    dropZone.addEventListener("drop", (e) => {
      e.preventDefault();
      fileInput.files = e.dataTransfer.files;
      fileNameDisplay.textContent = "Selected: " + fileInput.files[0].name;
      dropZone.style.backgroundColor = "";
    });
    fileInput.addEventListener("change", () => {
        if (fileInput.files.length > 0) {
        fileNameDisplay.textContent = "Selected: " + fileInput.files[0].name;
      }
    });