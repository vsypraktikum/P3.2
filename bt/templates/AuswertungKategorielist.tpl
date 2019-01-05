<!-- Template -->
<!-- Projekt -->
<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Kategorieverzeichnis
   </h2>
   <div id="idContentArea" class="clContentArea">
   </div>

   <div id="idButtonArea" class="clButtonArea">
      <select id = "kategorie_auswertung_name" name>
         @var rows_proj = context['data'];@
         @console.log(rows_proj);@
         @for var key_p in rows_proj@
            <option value="#key_p#">#key_p# </option>
         @endfor@
      </select>
      <button data-action="auswerten_kategorie" class="clButton">auswerten</button>
   </div>

</div>

<!-- EOF -->