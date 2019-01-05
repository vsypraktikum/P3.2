<!-- Template -->
<!-- Projekt -->
<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Auswertung Projektverzeichnis
   </h2>
   <div id="idContentArea" class="clContentArea">

   </div>
   <div id="idButtonArea" class="clButtonArea">
      <select id = "projekt_auswertung_name" name>
         @var rows_proj = context['data'];@
         @console.log(rows_proj);@
         @for var key_p in rows_proj@
            @var row_proj = rows_proj[key_p];@
            <option value="#key_p#">#row_proj['name']# </option>
         @endfor@
      </select>
      <button data-action="auswerten_projekt" class="clButton">auswerten</button>
   </div>
</div>

<!-- EOF -->