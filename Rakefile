require 'html-proofer'  # https://github.com/gjtorikian/html-proofer/

task default: %w[test]

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => true,
              :allow_hash_href => true,
              file_ignore: [],
              url_ignore: [],
              :typhoeus => {
                  :ssl_verifypeer => false,
                  :ssl_verifyhost => 0}
  }
  HTMLProofer.check_directory("./_site", options).run
end
