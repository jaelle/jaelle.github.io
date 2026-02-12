# Monkeypatch to support Liquid 4.0.3 and older on Ruby 3.2+
# Ruby 3.2 removed the tainted? method; Liquid 4.0.3 still tries to use it.
# This provides a shim so Jekyll builds succeed without upgrading Liquid.

unless Object.method_defined?(:tainted?)
  Object.define_method(:tainted?) { false }
end
