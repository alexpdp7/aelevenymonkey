if (document.URL.startsWith("https://wumo.com")) {
    transcript = data["Wumo"][document.URL];
    if(transcript) {
        edit_url = "https://github.com/alexpdp7/aelevenymonkey/edit/main/transcripts/" + document.URL.slice(8) + ".md" ;
        transcript += "Visit <a href=\"" + edit_url + "\">" + edit_url + "</a> to edit the transcript.";
    }
    else {
        add_url = "https://github.com/alexpdp7/aelevenymonkey/new/main/?filename=transcripts/" + document.URL.slice(8) + ".md"
        transcript = "No transcript found. Visit <a href=\"" + add_url + "\">" + add_url + "</a> to add a transcript.";
    }
    document.getElementsByTagName("article")[0].innerHTML = transcript + document.getElementsByTagName("article")[0].innerHTML;
}
