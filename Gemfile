source "https://rubygems.org"

gem "jekyll", "~> 4.3.2" # ✅ Use a modern Jekyll version

# Plugins and themes
gem "minimal-mistakes-jekyll", "~> 4.24.0"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-include-cache"  # ✅ Required for 'include_cached'
  gem "jekyll-remote-theme"
end

# Windows & JRuby platform support
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Windows file watcher performance
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock http_parser for JRuby builds
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
