<!-- Template -->
<form id="idForm" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Projektverzeichnis / Formular
   </h2>
   <div id="idContentArea" class="clContentArea">

   <input type="hidden" value="#context.data.id#" id="id_s" name="id_s" />
   <div class="clFormRow">
      <label for="name_s">Name <span class="clRequired"></span></label>
      <input type="text" value="#context.data.name#" id="name_s" name="name_s" autofocus required />
   </div>
   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="back" class="clButton">Zurück</button>
      <button data-action="save" class="clButton">Speichern</button>
   </div>
</form>
<!-- EOF -->