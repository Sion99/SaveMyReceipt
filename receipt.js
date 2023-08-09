const modal = document.getElementById('modal');
const closeModalBtn = document.getElementById('close-modal');
const realSubmitBtn = document.getElementById('realSubmit');
const fileInput = document.getElementById('chooseFile');
var container;

closeModalBtn.addEventListener('click', () => {
	modal.style.display = "none";
	document.body.style.overflow = "auto";
	container.innerHTML = '';
})

realSubmitBtn.onclick = uploadFile;

function uploadFile() {
	const formData = new FormData;
	var file = fileInput.files[0];
	formData.append('file', file);
	fetch('http://ec2-13-124-154-116.ap-northeast-2.compute.amazonaws.com:8000/post', {
		method: 'POST',
		cache: 'no-cache',
		body: formData // body 부분에 폼데이터 변수를 할당
	})
		.then((response) => response.json())
		.then((data) => {
			console.log(data);
		});
}


function loadFile(input) {
	modal.style.display = "block";
	document.body.style.overflow = "hidden";
	var file = input.files[0];

	var newImage = document.createElement("img");
	newImage.setAttribute("class", 'image-show');
	newImage.src = URL.createObjectURL(file);
	container = document.getElementById('image-show');
	container.appendChild(newImage);
};