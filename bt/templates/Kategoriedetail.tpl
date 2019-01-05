<!-- Template -->
<form id="idForm" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Kategorieverzeichnis / Formular
   </h2>
   <div id="idContentArea" class="clContentArea">

   <input type="hidden" value="#context.data.id#" id="id_s" name="id_s" />
   <div class="clFormRow">
      <label for="fehlerbeschreibung_s">Fehlerbeschreibung <span class="clRequired"></span></label>
      <input type="text" value="#context.data.fehlerbeschreibung#" id="fehlerbeschreibung_s" name="fehlerbeschreibung_s" autofocus required />
   </div>
  <div class="clFormRow">
      <label for="fehlerursache_s">Fehlerursache <span class="clRequired"></span></label>
      <input type="text" value="#context.data.fehlerursache#" id="fehlerursache_s" name="fehlerursache_s"  required />
   </div>
   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="back" class="clButton">Zurück</button>
      <button data-action="save" class="clButton">Speichern</button>
   </div>
</form>
<!-- EOF -->