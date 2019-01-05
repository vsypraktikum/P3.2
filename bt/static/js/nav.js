// ----------------------------------------------
// Beispiel lit-x
// nav.js
// ----------------------------------------------

// ----------------------------------------------
APP.Nav_cl = class {
// ----------------------------------------------
   constructor () {
   }
   render_px () {
      // zur Vereinfachung hier direkt den Inhalt des
      // Navigationsbereichs anzeigen und die Ereignisverarbeitung einrichten
      $.ajax({
         dataType: "json",
         url: '/navigation',
         type: 'GET',
         context: this
      })
      .done(function (data_opl) {
         this.doRender_p(data_opl);
         this.initHandler_p();
      })
      .fail(function(jqXHR_opl, textStatus_spl) {
         alert( "[Nav_cl] Fehler bei Anforderung: " + textStatus_spl );
      });
   }
   doRender_p (data_opl) {
      let markup_s = APP.tm_o.execute_px('nav.tpl', data_opl);
      $('#idNav').html(markup_s);
   }
   initHandler_p () {
      // Ereignisverarbeitung für die Schalter einrichten
      $("#idNav").on("click", "a", function (event_opl) {
         var action_s = $(event_opl.target).attr('data-action');
         // Weiterleitung! Das Nav-Objekt ist nicht für die Bearbeitung direkt verantwortlich
         APP.es_o.publish_px('app', [action_s, null]);
         // Weiterleitung und Standardbearbeitung unterbinden
         event_opl.stopPropagation();
         event_opl.preventDefault();
      });
   }
}
// EOF