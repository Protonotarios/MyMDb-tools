javascript:var movietitle = document.title;
 var movietitle = movietitle.replace(/"/g, "");
 var movietitle = movietitle.slice(0,movietitle.lastIndexOf("("));
 location.href='http://meta.protonotarios.eu/wiki/index.php?title=Special:FormEdit/Movie/'
  +encodeURIComponent(movietitle);
