{{- define "library-chart.labels" -}}
app: {{ .Chart.Name }}
release: {{ .Release.Name }}
{{- end }}

{{- define "library-chart.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}
