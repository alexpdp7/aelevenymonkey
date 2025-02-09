if (document.URL.startsWith("https://www.xkcd.com") || document.URL.startsWith("https://xkcd.com")) {
    if (document.URL.endsWith("xkcd.com/")) {
	// last strip
	prev = document.getElementsByClassName("comicNav")[0].children[1].children[0].attributes.href.nodeValue.replaceAll("/", "");
	index = Number.parseInt(prev) + 1;
    }
    else {
	index = Number.parseInt(document.URL.slice(document.URL.search("xkcd.com") + 9).replace("/", "")); 
    }

    explain_url = "https://www.explainxkcd.com/wiki/index.php/" + index+ "#Transcript";

    document.getElementById("ctitle").insertAdjacentHTML("afterend", "<p>View <a href=\"" + explain_url + "\">the transcript on explain xkcd</a>.</p>"); 
}
