{{- define "library-chart.deployment" -}}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "library-chart.fullname" . }}
  labels:
    {{- include "library-chart.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicas }}
  selector:
    matchLabels:
      app: {{ .Chart.Name }}
  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
          ports:
            - containerPort: {{ .Values.service.port }}
{{- end }}
