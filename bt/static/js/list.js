// ----------------------------------------------
// Beispiel lit-x
// list.js
// ----------------------------------------------

// ----------------------------------------------
APP.ListView_cl = class {
// ----------------------------------------------
   constructor (name_spl, path_spl, template_spl) {
      this.name_s = name_spl;
      this.path_s = path_spl;
      this.template_s = template_spl;
   }
   canClose_px () {
      return true;
   }
   close_px () {
      this.exitHandler_p();
   }
   render_px (data_opl) {
      // Parameter data_opl wird hier nicht benötigt
      // Anforderung an den Server senden
      $.ajax({
         dataType: "json",
         url: this.path_s,
         type: 'GET',
         context: this
      })
      .done(function (data_opl) {
         this.doRender_p(data_opl);
         this.initHandler_p();
         this.initList_p();
      })
      .fail(function(jqXHR_opl, textStatus_spl) {
         alert( "[Liste] Fehler bei Anforderung: " + textStatus_spl );
      });
   }
   doRender_p (data_opl) {
      // json-Daten bereits in js-Objekte umgesetzt
      var markup_s = APP.tm_o.execute_px(this.template_s, data_opl);
      $("#idContentOuter").html(markup_s);
   }
   initList_p () {
      this.rowId_s = ""; // id der selektierten Zeile
      // Buttons teilweise deaktivieren, bis eine Zeile ausgewählt wurde
      this.disableButtons_p();
   }
   initHandler_p () {
      // Ereignisverarbeitung einrichten

      // Ereignisverarbeitung für die Tabelle einrichten
      // man beachte: für jquery muss man CSS-Selektoren angeben, also #idList statt einfach nur idList !
      $("#idList").on("click", "td", $.proxy(this.onClickList_p, this));

      // Ereignisverarbeitung für die Schalter einrichten
      $("#idListContent #idButtonArea").on("click", "button", $.proxy(this.onClickButtons_p, this));

   }
   exitHandler_p () {
      // Ereignisverarbeitung aufheben
      $("#idList").off("click", "td", $.proxy(this.onClickList_p, this));
      $("#idListContent #idButtonArea").off("click", "button", $.proxy(this.onClickButtons_p, this));
   }
   onClickList_p (event_opl) {
      // hier werden nur click-Events auf td-Elemente geliefert
      if (this.rowId_s != "") {
         $("#"+this.rowId_s).removeClass("clSelected"); // Achtung: jetzt ist nur die Bezeichnung der CSS-Klasse gemeint!
      }
      this.rowId_s = $(event_opl.target).parent().attr('id');
      $("#"+this.rowId_s).addClass("clSelected");

      this.enableButtons_p();
   }
   onClickButtons_p (event_opl) {

      var action_s = $(event_opl.target).attr("data-action");
      switch (action_s) {
      case 'add':
         // weiterleiten
         APP.es_o.publish_px('app', [this.name_s+'.'+action_s, null]);
         break;
      case 'edit':
         APP.my_bool = true;
         if (this.rowId_s != "") {
            // Weiterleiten
            APP.es_o.publish_px('app', [this.name_s+'.'+action_s, this.rowId_s]);
         } else {
            alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
         }
         break;
      case 'delete':
         if (this.rowId_s != "") {
            if (confirm("Soll der Datensatz gelöscht werden?")) {
               // Id der selektierten Tabellenzeile anhängen
               var path_s = this.path_s + this.rowId_s; 
               $.ajax({
                  context: this,
                  dataType: "json",
                  url: path_s,
                  type: 'DELETE'
               })
               .done(function (data_opl) {
                  // Auswertung der Rückmeldung
                  // der umständliche Weg:
                  // - Liste neu darstellen, hier vereinfacht durch neue Anforderung
                  //APP.es_o.publish_px('list', ['refresh', null]);
                  
                  // einfacher mit direktem Entfernen der Zeile aus der Tabelle
                  // (id des gelöschten Eintrags wird in der Antwort geliefert)
                  $('#'+data_opl['id']).remove();
                  this.initList_p();
               })
               .fail(function(jqXHR_opl, textStatus_spl) {
                  alert( "[Liste] Fehler bei Anforderung: " + textStatus_spl );
               });
            }
         } else {
            alert("Wählen Sie bitte einen Eintrag in der Tabelle aus!");
         }
         break;
         case 'sort':
            var id = $("#projekt_name").val();
            $.ajax({
               dataType: "json",
               url: "Projektkomponente/" + id,
               type: 'GET',
               context: this
            })
            .done(function (data_opl){
               var markup_s = APP.tm_o.execute_px("Projektkomponentelist.tpl", data_opl);
               $("#idContentArea2").html(markup_s);
               console.log(markup_s);
            })
            break;
         case 'auswerten_projekt':
            var id = $("#projekt_auswertung_name").val();
             console.log(id);
            $.ajax({
               dataType: "json",
               url: "AuswertungProjekte/" + id,
               type: 'GET',
               context: this
            })
            .done(function (data_opl){
               var markup_s = APP.tm_o.execute_px("AuswertungProjekteTable.tpl", data_opl);
               $("#idContentArea").html(markup_s);
               console.log(markup_s);
            })
            break;
         case 'auswerten_kategorie':
            var id_kate = $("#kategorie_auswertung_name").val();
             console.log(id_kate);
            $.ajax({
               dataType: "json",
               url: "AuswertungKategorie/" + id_kate,
               type: 'GET',
               context: this
            })
            .done(function (data_opl){
               var markup_s = APP.tm_o.execute_px("AuswertungProjekteTable.tpl", data_opl);
               $("#idContentArea").html(markup_s);
               console.log(markup_s);
            })
         case 'auswerten_erkannt':
            var type_erkannt = $("#fehler_erkannt").val();
             console.log(type_erkannt);
            $.ajax({
               dataType: "json",
               url: "Fehler/?type=" + type_erkannt,
               type: 'GET',
               context: this
            })
            .done(function (data_opl){
               var markup_s = APP.tm_o.execute_px("FehlerTable.tpl", data_opl);
               $("#idContentArea2").html(markup_s);
               console.log(markup_s);
            })
         case 'auswerten_behoben':
            var type_behoben = $("#fehler_behoben").val();
             console.log(type_behoben);
            $.ajax({
               dataType: "json",
               url: "Fehler/?type=" + type_behoben,
               type: 'GET',
               context: this
            })
            .done(function (data_opl){
               var markup_s = APP.tm_o.execute_px("FehlerTable.tpl", data_opl);
               $("#idContentArea2").html(markup_s);
               console.log(markup_s);
            })


      }
      // Weiterleitung und Standardbearbeitung unterbinden
      event_opl.stopPropagation();
      event_opl.preventDefault();
   }
   // stärkere Einschränkung mit #idListContent notwendig, damit nicht die Buttons auf dem
   // Formular ebenfalls geändert werden
   enableButtons_p () {
      $("#idListContent #idButtonArea button").each(function () {
         if ($(this).attr("data-action") != "add" ){
            $(this).prop("disabled", false);
         }
      });
   }
   disableButtons_p () {
      $("#idListContent #idButtonArea button").each(function () {
         if ($(this).attr("data-action") != "add" && $(this).attr("data-action") != "sort" && $(this).attr("data-action") != "auswerten_projekt" && $(this).attr("data-action") != "auswerten_kategorie" && $(this).attr("data-action") != "auswerten_erkannt" && $(this).attr("data-action") != "auswerten_behoben")   {
            $(this).prop("disabled", true);
         }
      });
   }
}
// EOF