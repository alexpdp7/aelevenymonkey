if (document.URL.startsWith("https://www.penny-arcade.com")) {
    if(Object.hasOwn(penny_arcade_data, document.URL)) {
	edit_url = "https://github.com/alexpdp7/aelevenymonkey/edit/main/transcripts/" + document.URL.slice(8) + ".md" ;
	transcript = penny_arcade_data[document.URL];
	transcript += "Visit <a href=\"" + edit_url + "\">" + edit_url + "</a> to edit the transcript.";
    }
    else {
	add_url = "https://github.com/alexpdp7/aelevenymonkey/new/main/?filename=transcripts/" + document.URL.slice(8) + ".md"
	transcript = "No transcript found. Visit <a href=\"" + add_url + "\">" + add_url + "</a> to add a transcript.";
    }
    document.getElementsByClassName("comic-area")[0].innerHTML = transcript + document.getElementsByClassName("comic-area")[0].innerHTML; 
}
