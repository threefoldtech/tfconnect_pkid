
{{- define "image" -}}
{{ .Values.image.repo}}:{{.Values.image.tag }}
{{- end -}}

{{- define "releaseName" -}}
{{ $.Chart.Name}}-{{.Values.environment }}
{{- end -}}
