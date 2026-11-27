// Baut Aviasales-Suchlinks mit deinem Marker -> Provision pro Buchung
(function(){
  var C = window.REISE_CONFIG || {};
  function ddmm(v){ if(!v) return ""; var p=v.split("-"); return p[2]+p[1]; }
  window.flugSuche = function(e){
    e.preventDefault();
    var f=e.target, von=f.von.value.trim().toUpperCase(), nach=f.nach.value.trim().toUpperCase();
    if(von===nach){alert("Abflug- und Zielflughafen sind gleich – bitte ein anderes Ziel wählen.");return;}
    var pfad = von + ddmm(f.hin.value) + nach + ddmm(f.rueck.value) + (f.pax.value||"1");
    var url = "https://www.aviasales.com/search/" + pfad + "?marker=" + encodeURIComponent(C.marker||"") + "&locale=de&currency=eur";
    window.open(url,"_blank","noopener");
  };
  window.flugZiel = function(von,nach){
    var url="https://www.aviasales.com/search/"+von+nach+"1?marker="+encodeURIComponent(C.marker||"")+"&locale=de&currency=eur";
    window.open(url,"_blank","noopener");
  };
  document.addEventListener("DOMContentLoaded",function(){
    document.querySelectorAll("[data-partner]").forEach(function(a){
      var k=a.getAttribute("data-partner"); if(C[k]) a.href=C[k];
      a.target="_blank"; a.rel="sponsored noopener";
    });
    var d=new Date(); d.setDate(d.getDate()+21);
    var hin=document.querySelector("input[name=hin]"); if(hin&&!hin.value) hin.value=d.toISOString().slice(0,10);
  });
})();
