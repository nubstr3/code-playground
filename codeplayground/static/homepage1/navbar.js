const homepageButton = document.getElementById('HomeButton');
const aboutButton = document.getElementById('AboutButton');
const contactButton = document.getElementById('ContactButton');


homepageButton.addEventListener('click', () => {
	document.getElementById('HomeShow').style.display="block";
    document.getElementById('AboutShow').style.display="none";
    document.getElementById('ContactShow').style.display="none";
});

aboutButton.addEventListener('click', () => {
	document.getElementById('HomeShow').style.display="none";
    document.getElementById('AboutShow').style.display="block";
    document.getElementById('ContactShow').style.display="none";
});

contactButton.addEventListener('click', () => {
	document.getElementById('HomeShow').style.display="none";
    document.getElementById('AboutShow').style.display="none";
    document.getElementById('ContactShow').style.display="block";
});
