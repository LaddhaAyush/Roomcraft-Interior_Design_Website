function showNext(section) {
    document.getElementById('dimensions-form').style.display = 'none';
    document.getElementById('sofa-selection').style.display = 'none';
    document.getElementById('furniture-selection').style.display = 'none';
    document.getElementById('lighting-selection').style.display = 'none';
    document.getElementById('paint-selection').style.display = 'none';
    
    document.getElementById(section).style.display = 'block';
}

function showPrev(section) {
    document.getElementById('dimensions-form').style.display = 'none';
    document.getElementById('sofa-selection').style.display = 'none';
    document.getElementById('furniture-selection').style.display = 'none';
    document.getElementById('lighting-selection').style.display = 'none';
    document.getElementById('paint-selection').style.display = 'none';

    document.getElementById(section).style.display = 'block';
}

function submitForm() {
    const formData = new FormData();
    formData.append('width', document.getElementById('width').value);
    formData.append('length', document.getElementById('length').value);
    const selectedSofaType = document.querySelector('input[name="sofa-type"]:checked');
    if (selectedSofaType) {
        formData.append('sofaType', selectedSofaType.value);
    } else {
        alert("Please select a bed type");
        return; // Stop form submission if no bed type is selected
    }
    formData.append('furniture', JSON.stringify(Array.from(document.querySelectorAll('input[name="living-area-furniture[]"]:checked')).map(el => el.value)));
    formData.append('lighting', JSON.stringify(Array.from(document.querySelectorAll('input[name="living-area-lighting[]"]:checked')).map(el => el.value)));
    formData.append('paint', document.querySelector('input[name="paint-type"]:checked').value);

    fetch('/submitBedroom', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            alert('Form submitted successfully!');
        } else {
            alert('Failed to submit form');
        }
    })
    .catch(error => console.error('Error:', error));
}


$(function() {
    $('#width').on('input', function() {
        $('#width-input').val($(this).val());
    });
    $('#length').on('input', function() {
        $('#length-input').val($(this).val());
    });
});