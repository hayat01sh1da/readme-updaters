# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def test_run
    assert_equal(0, Application.run)
  end
end
