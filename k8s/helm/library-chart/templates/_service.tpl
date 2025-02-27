{{- define "library-chart.service" -}}
apiVersion: v1
kind: Service
metadata:
  name: {{ include "library-chart.fullname" . }}
  labels:
    {{- include "library-chart.labels" . | nindent 4 }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: {{ .Values.service.port }}
  selector:
    app: {{ .Chart.Name }}
{{- end }}
