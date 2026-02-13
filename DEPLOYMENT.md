# Deployment Guide

This guide covers deploying the First Aid Assistant to various platforms.

## ⚠️ Important Notes

Before deploying:

1. **Medical Disclaimer**: Ensure all pages have clear medical disclaimers
2. **Model Training**: Replace heuristic classifier with trained model
3. **Legal Review**: Consult legal counsel for liability issues
4. **Testing**: Thoroughly test with diverse images
5. **Security**: Implement rate limiting, file validation, HTTPS

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py

# Access at http://127.0.0.1:5000
```

## Deployment Options

### 1. Heroku (Free Tier Available)

**Pros**: Easy deployment, free tier, built-in HTTPS
**Cons**: Cold starts, limited resources

**Steps**:

1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Update `requirements.txt`:
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

3. Deploy:
```bash
# Login to Heroku
heroku login

# Create app
heroku create first-aid-assistant-demo

# Deploy
git push heroku main

# Open
heroku open
```

4. Configure:
```bash
heroku config:set FLASK_ENV=production
```

### 2. Google Cloud Platform (Cloud Run)

**Pros**: Serverless, scales automatically, pay-per-use
**Cons**: Requires GCP account, billing setup

**Steps**:

1. Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
```

2. Deploy:
```bash
# Build and deploy
gcloud run deploy first-aid-assistant \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 3. AWS (Elastic Beanstalk)

**Pros**: Scalable, integrates with AWS services
**Cons**: More complex setup, costs

**Steps**:

1. Install EB CLI:
```bash
pip install awsebcli
```

2. Initialize:
```bash
eb init -p python-3.11 first-aid-assistant
eb create first-aid-assistant-env
```

3. Deploy:
```bash
eb deploy
```

### 4. DigitalOcean App Platform

**Pros**: Simple, affordable, good documentation
**Cons**: Limited free tier

**Steps**:

1. Create `app.yaml`:
```yaml
name: first-aid-assistant
services:
- name: web
  github:
    repo: your-username/first-aid-assistant
    branch: main
  run_command: gunicorn --worker-tmp-dir /dev/shm app:app
  environment_slug: python
  instance_size_slug: basic-xxs
  instance_count: 1
  http_port: 8080
  routes:
  - path: /
```

2. Deploy via dashboard or CLI

### 5. Railway

**Pros**: Very simple, generous free tier
**Cons**: Newer platform

**Steps**:

1. Connect GitHub repo
2. Railway auto-detects Python
3. Deploy automatically

### 6. Render

**Pros**: Free tier, easy setup, HTTPS included
**Cons**: Limited free tier resources

**Steps**:

1. Create `render.yaml`:
```yaml
services:
  - type: web
    name: first-aid-assistant
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

2. Connect GitHub and deploy

## Production Checklist

### Security

- [ ] Enable HTTPS (SSL/TLS)
- [ ] Implement rate limiting
- [ ] Add CSRF protection
- [ ] Validate file uploads strictly
- [ ] Set max file size
- [ ] Sanitize all inputs
- [ ] Use environment variables for secrets
- [ ] Implement logging
- [ ] Add error monitoring (Sentry)

### Performance

- [ ] Enable caching
- [ ] Compress responses (gzip)
- [ ] Optimize images
- [ ] Use CDN for static files
- [ ] Implement database connection pooling
- [ ] Add request timeouts
- [ ] Monitor response times

### Reliability

- [ ] Set up health checks
- [ ] Implement graceful shutdowns
- [ ] Add backup/restore procedures
- [ ] Set up monitoring (Datadog, New Relic)
- [ ] Configure auto-scaling
- [ ] Set up alerts
- [ ] Document incident response

### Legal & Compliance

- [ ] Add Terms of Service
- [ ] Add Privacy Policy
- [ ] Include medical disclaimer on every page
- [ ] Implement age verification
- [ ] Add cookie consent (if applicable)
- [ ] Document data retention policy
- [ ] Consult legal counsel

## Environment Variables

Create `.env` file (never commit this):

```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
MAX_UPLOAD_SIZE=16777216  # 16MB
ALLOWED_EXTENSIONS=png,jpg,jpeg,gif,webp
MODEL_PATH=models/injury_classifier.h5
```

Load in `app.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_UPLOAD_SIZE', 16777216))
```

## Database Setup (Optional)

For storing analysis history:

```python
# Using SQLite for development
import sqlite3

# Using PostgreSQL for production
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    # Don't store actual images for privacy
```

## Monitoring Setup

### Using Sentry for Error Tracking

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
```

### Using Prometheus for Metrics

```python
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)
```

## CDN Setup for Static Files

Using Cloudflare:

1. Sign up for Cloudflare
2. Add your domain
3. Enable CDN
4. Update DNS
5. Configure caching rules

## Custom Domain Setup

1. Purchase domain (Namecheap, Google Domains)
2. Configure DNS:
   - Add A record pointing to server IP
   - Add CNAME for www
3. Configure SSL certificate
4. Update app configuration

## Scaling Considerations

### Horizontal Scaling

```python
# Use Gunicorn with multiple workers
gunicorn --workers 4 --threads 2 --bind 0.0.0.0:8080 app:app
```

### Load Balancing

Use platform load balancer or:
- NGINX
- HAProxy
- AWS ALB/ELB

### Caching Layer

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/api/info')
@cache.cached(timeout=300)
def get_info():
    # Cached for 5 minutes
    pass
```

## Backup Strategy

1. Database backups (daily)
2. Model file backups (on update)
3. Configuration backups (on change)
4. Off-site storage (S3, Cloud Storage)

## Rollback Plan

1. Tag releases: `git tag v1.0.0`
2. Keep previous versions deployed
3. Quick rollback command ready
4. Test rollback procedure

## Cost Estimation

### Free Tier Options

- Render: 750 hours/month free
- Railway: $5 credit/month
- Heroku: 550-1000 dyno hours/month

### Paid Tier (Estimated)

- AWS: $10-50/month (t2.micro)
- GCP: $10-40/month (Cloud Run)
- DigitalOcean: $5-12/month (basic droplet)

## Support & Maintenance

- Monitor error rates
- Review logs weekly
- Update dependencies monthly
- Security patches immediately
- User feedback review
- Performance optimization quarterly

## Additional Resources

- [Flask Deployment Documentation](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [12 Factor App Methodology](https://12factor.net/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Security Best Practices](https://developer.mozilla.org/en-US/docs/Web/Security)

---

Remember: This is a demo project. For actual medical use, consult with healthcare professionals and legal counsel before deployment.
