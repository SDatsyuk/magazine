function onHover(id){
	console.log(id);
	var t = document.getElementById(id).getAttribute('src');
	console.log(t);
	$('#productImage').attr('src', t);
}