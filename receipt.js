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

realSubmitBtn.onclick = sendImageToEC2;

async function sendImageToEC2() {
	const ec2Url = 'https://sions.me/post'; // EC2 인스턴스의 URL로 대체

	// Create a FormData object and append the image file
	const formData = new FormData();
	formData.append('image', fileInput.files[0]);

	try {
		const response = await fetch(ec2Url, {
			method: 'POST',
			body: formData,
		});

		if (response.ok) {
			const responseData = await response.json();
			console.log('Response from EC2:', responseData);
		} else {
			console.error('Error sending image to EC2:', response.statusText);
		}
	} catch (error) {
		console.error('Error:', error);
	}
}

// // Usage example:
// const inputFile = document.querySelector('#imageInput'); // Assuming you have an input element with type="file"
// inputFile.addEventListener('change', (event) => {
// 	const selectedFile = event.target.files[0];
// 	if (selectedFile) {
// 		sendImageToEC2(selectedFile);
// 	}
// });


async function uploadFile() {
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
